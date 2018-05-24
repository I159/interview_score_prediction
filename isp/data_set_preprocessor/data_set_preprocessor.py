"""
Data architecture agnostic tools.

Implementations of possible transformations of a data set to reach several
goals:
    * Make data set numeric as possible
    * Remove broken data
    * Prepare for binary prediction modeling
"""
import os

from pandas import read_csv
import pandas
import numpy as np


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
