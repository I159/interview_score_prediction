"""
Data architecture agnostic modeling tool set.

Build automated model for binary prediction.
"""
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.model_selection import train_test_split


FEATURES_NUM = 6


def build_feature_model(train_set, test_set):
    selection_test = SelectKBest(score_func=chi2, k=FEATURES_NUM)
    fit = selection_test.fit(train_set, test_set)
    return fit.transform(train_set)


def learn(data_set):
    train_set, test_set = train_test_split(data_set, test_size=0.33)
    train_set = build_feature_model(train_set, test_set)
    __import__('pdb').set_trace()
    return
