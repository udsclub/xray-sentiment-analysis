from sklearn.base import TransformerMixin
from sklearn.pipeline import Pipeline, FeatureUnion

from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize

class Lemmatizer(TransformerMixin):
    def __init__(self, key='text', lemmatizer = WordNetLemmatizer()):
        """
        Arguments:
        key -- stands for which column to proceed
        lemmatizer -- which stemmer to use, default is WordNetLemmatizer
        """
        self.key = key
        self.lemmatizer = lemmatizer

    def transform(self, X):
        """
        Clean text column provided in initialization, as key from useless text.

        Arguments:
        X -- Pandas Dataframe
        """
        processed = X[self.key].apply(self.transform_text)
        return X.assign(**{self.key: processed})

    def transform_text(self, text):
        tokens = word_tokenize(text)
        # ignore words less than 3 letters
        stemmed = [self.perform_stem(w) for w in tokens if len(w) > 1]
        return ' '.join(stemmed)

    def perform_stem(self, word):
        try:
            # print("%s                                           \r"%(word), end="")
            return self.lemmatizer.lemmatize(word)
        except:
            print("Processing: '%s'" % word)
            raise

    def fit(self, *_):
        return self
