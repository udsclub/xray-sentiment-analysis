## SGDClassifier


pretrained model_mix SGDClassifier (.pkl format)
https://drive.google.com/open?id=0B0NR6sIylAi1d18xdzJIX0llWjg





| | Preprocess | val_acc on RT | test_acc on IMDB | val_acc on IMDB | test_acc on RT | val_acc on MIX(RT+IMDB) | test_acc on MIX
| ------------- |:------------------:| -----:|:--------:|:----|:--------:|:--------:|:--------:|
| 1 | regExp + CountVectorizer() | 0.7823 | 0.8430 | 0.8371 | 0.8371 | 0.6910 | |
| 2 | 1 + stop_words='english' | 0.7758 | 0.8320 | 0.8755 | 0.6979 | |
| 3 | 2 + ngram_range=(1,2) | 0.7819 | 0.8512 | 0.8883 | 0.6848 | |
| 4 | CountVectorizer() + stop_words='SLM' + ngram_range=(1,2) | 0.7884 | 0.8236 | 0.8948 | 0.6785 | |
| 5 | 3 + stop_words='SLM' + TfIdfTransformer() | 0.7345 | 0.8295 | 0.9015 | 0.7524 | |
| 6 | 5 + TfIdfTransformer(sublinear_tf=True) | 0.7319 | 0.8438 | 0.9059 | 0.7565 | |
