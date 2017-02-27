from sklearn.base import TransformerMixin
from sklearn.pipeline import Pipeline, FeatureUnion

from nltk.stem.porter import PorterStemmer as DefaultStemmer
from nltk import word_tokenize

class Stemmer(TransformerMixin):
    def __init__(self, key='text', stemmer = DefaultStemmer()):
        """
        Arguments:
        key -- stands for which column to proceed
        stemmer -- which stemmer to use, default is PorterStemmer
        """
        self.key = key
        self.stemmer = stemmer

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
            return self.stemmer.stem(word)
        except:
            print("Processing: '%s'" % word)
            raise

    def fit(self, *_):
        return self
