## SGDClassifier


pretrained model_mix SGDClassifier (.pkl format)
https://drive.google.com/open?id=0B0NR6sIylAi1d18xdzJIX0llWjg



#### Train/Test stages:

| Step  | Preprocess | val_acc on RT | test_acc on IMDB | val_acc on IMDB | test_acc on RT 
| ------------- |:------------------ | :-----:|:--------:|:----|:--------:
| 1 | regExp + CountVectorizer() | 0.7823 | 0.8430 | 0.8371 | 0.6910 
| 2 | Step 1 + stop_words='english' | 0.7758 | 0.8320 | 0.8755 | 0.6979
| 3 | Step 2 + ngram_range=(1,2) | 0.7819 | 0.8512 | 0.8883 | 0.6848
| 4 | CountVectorizer() + STOPWORDS + ngram_range=(1,2) | 0.7884 | 0.8236 | 0.8948 | 0.6785
| 5 | Step 3 + STOPWORDS + TfIdfTransformer() | 0.7345 | 0.8295 | 0.9015 | 0.7524
| 6 | Step 5 + TfIdfTransformer(sublinear_tf=True) | 0.7319 | 0.8438 | 0.9059 | 0.7565

STOPWORDS = 'a','an','by','did','does', 'was', 'were', 'i' 



#### Train/Test stages for MIX:

| Step | Preprocess | val_acc on MIX(RT+IMDB) | val_acc on RT | val_acc on IMDB
| ------------- |:------------------ | :-----:|:--------:|:----|:--------:
| 7 | Step 6 | 0.7770 | 0.7871 |  0.8958
