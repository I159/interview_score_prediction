import os

from pandas import read_csv
import pandas
import numpy as np


SCORE = 'score'
DATE = 'invitationDate'
APPLICATION_TIME = 'applicationTime'
IS_RETAKE = 'isRetake'

DATA_SET_FILE = 'application_data.csv'


def parse_csv():
    path = os.path.join(
        os.path.dirname(
            os.path.dirname(__file__)),
        DATA_SET_FILE)
    return read_csv(path, delimiter=',')


def score_to_boolean(data_set):
    data_set[SCORE] = data_set[SCORE].astype(float)
    # FIXME: a brave assumption that "to be better than average is enough to be
    # hired". The only point it was chosen - this simplification allows to
    # abstract form exact values.
    mean_score = data_set[SCORE].mean()
    data_set[SCORE] = np.where(data_set[SCORE] > mean_score, 1, 0)
    return data_set


def datetime_to_timestamp(data_set):
    data_set[DATE] = pandas.to_datetime(data_set[DATE]).astype(np.int64)
    data_set[APPLICATION_TIME] = pandas.to_datetime(data_set[APPLICATION_TIME]).astype(np.int64)
    return data_set

def bool_to_num(data_set):
    data_set[IS_RETAKE] = data_set[IS_RETAKE].astype(int)
    return data_set

def drop_unnamed(data_set):
    """docstring for drop_unnamed"""
    data_set = data_set.loc[:, ~data_set.columns.str.contains('^Unnamed')]
    return data_set

def parse_data_set():
    data_set = parse_csv()
    data_set = score_to_boolean(data_set)
    data_set = datetime_to_timestamp(data_set)
    data_set = bool_to_num(data_set)
    data_set = drop_unnamed(data_set)
    __import__('pdb').set_trace()
    return data_set
