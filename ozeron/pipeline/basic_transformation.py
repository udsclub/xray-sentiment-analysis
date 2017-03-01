from sklearn.base import TransformerMixin
from sklearn.pipeline import Pipeline, FeatureUnion
import re

class BasicTransformation(TransformerMixin):
    def __init__(self, *args, key='text'):
        """Argument 'key', stands for which column to proceed"""
        self.key = key

    def transform(self, X):
        """
        Clean text column provided in initialization, as key from useless text.

        Arguments:
        X -- Pandas Dataframe
        """
        return X

    def fit(self, *_):
        return self
