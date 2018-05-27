"""
Data architecture agnostic tools.

Implementations of possible transformations of a data set to reach several
goals:
    * Make data set numeric as possible
    * Remove broken data
    * Prepare for binary prediction modeling
"""
import json
import os
import string

from pandas import read_csv
import pandas
import numpy as np
import nltk
from nltk.corpus import stopwords
from nltk.text import TextCollection


def parse_csv(file_name):
    path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)), file_name)
    return read_csv(path, delimiter=',')


def int_to_binary(data_set, column, threshold=None):
    data_set[column] = data_set[column].astype(float)
    threshold = data_set[column].mean() if threshold is None else threshold
    data_set[column] = np.where(data_set[column] > threshold, 1, 0)
    return data_set


def datetime_to_timestamp(data_set, *columns):
    for column in columns:
        data_set[column] = pandas.to_datetime(
            data_set[column]).astype(np.int64)
    return data_set


def bool_to_num(data_set, column):
    data_set[column] = data_set[column].astype(int)
    return data_set


def drop_unnamed(data_set):
    data_set = data_set.loc[:, ~data_set.columns.str.contains('^Unnamed')]
    return data_set


def extract_field(x, field):
    try:
        return ' '.join([i[field] for i in x])
    except Exception as e:
        print(x)


def extract_text(data_set, column, field):
    data_set[column] = data_set[column].apply(json.loads)
    data_set = data_set[getattr(data_set, column).apply(
        lambda x: isinstance(x, list))]
    data_set[column] = data_set[column].apply(extract_field, args=(field,))
    return data_set


def tokenize_text(data_set, column):
    stem = nltk.stem.SnowballStemmer('english')
    def tokenize(text):
        text = nltk.word_tokenize(text.lower())
        return [stem.stem(token) for token in text if token not in string.punctuation]

    data_set[column] = data_set[column].apply(tokenize)
    return data_set


def vectorize_corpus(data_set):
    # TODO: apply to whole series
    texts = TextCollection(corpus)
    for doc in corpus:
        yield {
            term: texts.tf_idf(term, doc)
            for term in doc
        }


# def apply_tag(row, bow_field, tag_field):
    # tag = row[tag_field]
    # row[bow_field] = {i: tag for i in row[bow_field]}
    # return row


# def tag_words(data_set, bow_field, tag_field):
    # data_set = data_set.apply(apply_tag, axis=1, args=(bow_field, tag_field))
    # return data_set
