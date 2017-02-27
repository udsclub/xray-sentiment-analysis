from sklearn.base import TransformerMixin
from sklearn.feature_extraction.text import CountVectorizer

class DataframeVectorizer(TransformerMixin):
    def __init__(self, key='text', vectorizer=CountVectorizer()):
        """
        Arguments:
        key -- stands for which column to proceed
        vectorizer -- which stemmer to use, default is PorterStemmer
        """
        self.key = key
        self.vectorizer = vectorizer

    def transform(self, X):
        """
        Arguments:
        X -- Pandas Dataframe
        """
        return self.vectorizer.transform(X[self.key])

    def fit(self, X):
        """
        Arguments:
        X -- Pandas Dataframe
        """
        self.vectorizer.fit(X[self.key])
        return self
