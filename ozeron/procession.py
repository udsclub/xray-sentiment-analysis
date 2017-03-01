from sklearn.pipeline import Pipeline
from pipeline.text_cleaner import TextCleaner
from pipeline.stemmer import Stemmer

import pandas as pd
import pickle

def read(path):
    return pd.read_csv(path, sep="|")

def store(data, path):
    with open(path, 'wb') as f:
        pickle.dump(data, f)

def process_and_store(name):
    data_path = "data/%s.csv" % name
    processed_path = "data/processed/%s.bin" % name

    df = read(data_path)
    DataPipeline = Pipeline(steps=[
        ('clean_words', TextCleaner(key='text')),
        ('stem', Stemmer())
    ])

    X_after_data = DataPipeline.transform(df)
    store(X_after_data, processed_path)
