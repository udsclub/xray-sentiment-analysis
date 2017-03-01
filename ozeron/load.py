import pandas as pd
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.externals import joblib

from sklearn.pipeline import Pipeline, FeatureUnion

from pipeline.text_cleaner import TextCleaner
from pipeline.stemmer import Stemmer
from pipeline.dataframe_vectorizer import DataframeVectorizer

from utils import load_and_split, other_name, load_dumped

from sklearn import metrics
import pickle

def calculate_performance(trained, testing, X, y):
    X_processed = DataPipeline.transform(X)
    predicted = LearningPipeline.predict(X_processed)
    print('Performance %s on %s' % (trained, testing))
    print(metrics.classification_report(y, predicted))
    print('Accuracy: ', metrics.accuracy_score(y, predicted))
    return metrics.accuracy_score(y, predicted)

def calculate_stats(trained, testing):
    X_train, X_test, y_train, y_test = load_and_split(testing)
    return calculate_performance(trained, testing, X_test, y_test)

def perform(name):
    global DataPipeline
    global LearningPipeline
    with open('../dumps/%s__data.bin'% name, 'rb')  as f:
        DataPipeline = pickle.load(f)
    with open('../dumps/%s__learn.bin' % name, 'rb')  as f:
        LearningPipeline = pickle.load(f)

    val_acc = calculate_stats(name, name)
    test_acc = calculate_stats(name, other_name(name))
    return [val_acc, test_acc]

val_acc_rt, test_acc_rt = perform('reviews_rt_all')
val_acc_imdb, test_acc_imdb = perform('imdb_small')

print([val_acc_rt, test_acc_rt, val_acc_imdb, test_acc_imdb])
