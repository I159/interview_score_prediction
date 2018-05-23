import os

from pandas import read_csv
import numpy as np


def parse_csv():
    path = os.path.join(
        os.path.dirname(
            os.path.dirname(__file__)),
        'application_data.csv')
    return read_csv( path, delimiter=',')


def score_to_boolean(res):
    """docstring for prepare_set"""
    res['score'] = res['score'].astype(float)
    # FIXME: a brave assumption that "to be better than average is enough to be
    # hired". The only point it was chosen - this simplification allows to abstract form exact values.
    mean_score = res['score'].mean()
    res['score'] = np.where(res['score'] > mean_score, 1, 0)
    return res


def parse_data_set():
    data_set = parse_csv()
    return score_to_boolean(data_set)
