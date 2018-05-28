"""
Data architecture agnostic modeling tool set.

Build automated model for binary prediction.
"""
from sklearn.feature_selection import SelectKBest
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import chi2
from sklearn.model_selection import train_test_split
import nltk
from sklearn.feature_extraction import text


FEATURES_NUM = 6


def fit_text_model(train_set, column):
    vectorizer = text.TfidfVectorizer(min_df=1)

    def vectorize(text):
        return vectorizer.fit_transform(text)

    train_set[column] = train_set[column].apply(vectorize)
    # TODO: combine into a structure: [features, tag]
    return nltk.NaiveBayesClassifier.train(train_set)

def build_feature_model(data_set, bow_column):
    train_set, test_set = train_test_split(data_set, test_size=0.33)

    text_model = fit_text_model(test_set, bow_column)
    # TODO: use prediction of a text model as a field in the super-model

    selection_test = SelectKBest(score_func=chi2, k=FEATURES_NUM)
    fit = selection_test.fit(train_set, test_set)
    return fit.transform(train_set)


def learn(data_set, bow_column):
    bow_model = build_feature_model(data_set, bow_column)
    pass
