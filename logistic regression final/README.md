
|     |       Preprocess       |  RT+IMDB     |    RT |IMDB
| ------------- |:------------------:| -----:|:--------:|:----|
|  1   | Baseline(countvectorizer)    | 0.82 |  0.72 |0.89
|  2  | Data cleaning, stopwords, stemming  | 0.81   | 0.78 |0.88
| 3 | 2 + Hashing vectorizer       |   0.82   | 0.78|0.89
| 4 | 1+2+POS tags   | 0.81  | 0.77| 0.88
|  5     |1+2+Tfidf transformer+bigrams               | 0.83 |0.80|0.90
|6| 1+2+Grid search parameters | 0.84|0.79|0.85
| 7  |2+Tfidfvectorizer+bigrams     | 0.84 |0.80|0.91


