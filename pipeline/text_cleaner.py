from sklearn.base import TransformerMixin
from sklearn.pipeline import Pipeline, FeatureUnion
import re

class TextCleaner(TransformerMixin):
    def __init__(self, *args, key='text'):
        """Argument 'key', stands for which column to proceed"""
        self.key = key
        self.non_word_regex = re.compile('[^a-zA-Z\d\s:_]')
        self.tag_regex = re.compile('<[^>]*>')


    def transform(self, X):
        """
        Clean text column provided in initialization, as key from useless text.

        Arguments:
        X -- Pandas Dataframe
        """
        processed = X[self.key].apply(self.preprocess)
        return X.assign(**{self.key: processed})

    def preprocess(self, text):
        try:
            text = re.sub('-', ' ', text)
            text = self.tag_regex.sub(' ', text)
            text = self.non_word_regex.sub(' ', text)
            # WTF??
            # emoticons = re.findall('(?::|;|=)(?:-)?(?:\)|\(|D|P)', text)
            # text = re.sub('[\W]+', ' ', text.lower()) + ''.join(emoticons).replace('-', '')
            return text.lower()
        except TypeError as e:
            print("Received: %s – %s" % (type(text), text))
            raise

    def fit(self, *_):
        return self
