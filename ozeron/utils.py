import pandas as pd
import pickle
from sklearn.model_selection import train_test_split

def dump_model(path, model):
    with open(path, 'wb') as f:
        pickle.dump(model, f)

def load_dumped(path):
    result = None
    with open(path, 'rb') as f:
        result = pickle.load(f)
    return result

def load_file(name):
    path = "../data/%s.csv" % name
    df = pd.read_csv(path, sep="|")
    return df

def load_and_split(name):
    path = "../data/%s.csv" % name
    df = pd.read_csv(path, sep="|")
    return train_test_split(df[['text']], df['label'], test_size=0.2, random_state=42, stratify=df['label'])

def load_and_split_quick(name):
    path = "../data/%s.csv" % name
    df = pd.read_csv(path, sep="|")
    processed = load_dumped("../data/processed/%s.bin" % name)
    return train_test_split(df[['text']], df['label'], test_size=0.2, random_state=42, stratify=df['label'])


def other_name(name):
    other_dataset = 'imdb_small'
    if (name == 'imdb_small'):
        other_dataset = 'reviews_rt_all'
    return other_dataset
