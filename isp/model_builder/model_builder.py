from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.model_selection import train_test_split


FEATURES_NUM = 6


class FeatureModel:
    def __init__(self, data_set):
        self.raw_train_set, self.test_set = train_test_split(
            data_set, test_size=0.33)
        self._train_set = None

    def extract_features(self):
        selection_test = SelectKBest(score_func=chi2, k=FEATURES_NUM)
        fit = selection_test.fit(self.raw_train_set, self.test_set)
        return fit.transform(self.raw_train_set)

    @property
    def train_set(self):
        if not self._train_set:
            self._train_set = self.extract_features()
        return self._train_set


def learn(data_set):
    feature_model = FeatureModel(data_set)
