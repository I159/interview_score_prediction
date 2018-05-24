"""
Data architecture agnostic modeling tool set.

Build automated model for binary prediction.
"""
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.model_selection import train_test_split
import nltk


FEATURES_NUM = 6


def build_text_feature_model(data_set, bow_column):
    data_set = data_set[bow_column]
    train_set, _ = train_test_split(data_set, test_size=0.33)
    classifier = nltk.classify.DecisionTreeClassifier.train(
        train_set, entropy_cutoff=0, support_cutoff=0)
    return classifier


def build_feature_model(data_set):
    train_set, test_set = train_test_split(data_set, test_size=0.33)
    selection_test = SelectKBest(score_func=chi2, k=FEATURES_NUM)
    fit = selection_test.fit(train_set, test_set)
    return fit.transform(train_set)


def learn(data_set, bow_column):
    bow_model = build_text_feature_model(data_set, bow_column)
    __import__('pdb').set_trace()
    # train_set = build_feature_model(train_set, test_set)
    pass
