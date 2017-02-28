
import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LogisticRegressionCV
from sklearn.externals import joblib

from sklearn.pipeline import Pipeline, FeatureUnion

from pipeline.text_cleaner import TextCleaner
from pipeline.stemmer import Stemmer
from pipeline.dataframe_vectorizer import DataframeVectorizer

from utils import dump_model, load_and_split, other_name, load_and_split_quick

from sklearn import metrics
import pickle
import datetime

#global
DataPipeline = Pipeline(steps=[
        ('clean_words', TextCleaner(key='text')),
        ('stem', Stemmer()),
        ('vectorize', DataframeVectorizer(vectorizer=TfidfVectorizer()))])
#global
FastDataPipeline = Pipeline(steps=[('vectorize', DataframeVectorizer(vectorizer=TfidfVectorizer()))])

#global
LearningPipeline = Pipeline(steps=[
    ('logistic', LogisticRegressionCV(n_jobs=2,verbose=1))
])

def dump_models(name, f1_score, time_mark,
                data_pipeline=DataPipeline,
                learn_pipeline=LearningPipeline):
    path = 'dumps/history/%s__%s__%s__' % (name, time_mark, f1_score)
    dump_model(path + 'data.bin', data_pipeline)
    dump_model(path + 'learn.bin', learn_pipeline)
    path = 'dumps/%s__' % (name)
    dump_model(path + 'data.bin', data_pipeline)
    dump_model(path + 'learn.bin', learn_pipeline)

def store_results(name, y, predicted,
                  data_pipeline=DataPipeline,
                  learn_pipeline=LearningPipeline):
    acc = round(metrics.accuracy_score(y, predicted), 5)

    dt=datetime.datetime.now()
    time_mark = dt.strftime('%Y%m%d%H%M')

    dump_models(name, acc, time_mark,
                data_pipeline=data_pipeline,
                learn_pipeline=learn_pipeline)

def calculate_other_performance(name):
    other_dataset = other_name(name)
    X_train, X_test, y_train, y_test = load_and_split(other_dataset)
    calculate_performance(name, other_dataset, X_test, y_test)

def calculate_performance(trained, testing, X, y,
                         data_pipeline=DataPipeline,
                         learn_pipeline=LearningPipeline):
    X_processed = data_pipeline.transform(X)
    predicted = learn_pipeline.predict(X_processed)
    print('Performance %s on %s' % (trained, testing))
    print(metrics.classification_report(y, predicted))
    print('Accuracy: ', metrics.accuracy_score(y, predicted))
    return predicted

def train(name):
    data_pipeline = DataPipeline
    X_train, X_test, y_train, y_test = load_and_split(name)


    X_after_processing = data_pipeline.fit_transform(X_train)
    print("Data processed!")

    LearningPipeline.fit(X_after_processing, y_train)
    print("Models trained!")

    predicted = calculate_performance(name, name, X_test, y_test,
                                     data_pipeline=data_pipeline)
    store_results(name, y_test, predicted,
                  data_pipeline=data_pipeline)
    calculate_other_performance(name)


train('reviews_rt_all')

train('imdb_small')
