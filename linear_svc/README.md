## LinearSVC


pretrained model_mix LinearSVC (.pkl format)
https://drive.google.com/file/d/0B0NR6sIylAi1V1RKTVlWMXdGSzQ/view?usp=sharing



#### Train/Test stages:

| Step | Preprocess | val_acc on RT | test_acc on IMDB | val_acc on IMDB | test_acc on RT 
| ------------- |:------------------ | :-----:|:--------:|:----|:--------:
| 1 | CountVectorizer() | 0.76 | 0.81 | 0.86 | 0.68 
| 2 | regExp + CountVectorizer() | 0.76 | 0.81 | 0.86 | 0.68 
| 3 | CountVectorizer(ngram_range=(1, 2)) | 0.7962 | 0.8608 | 0.9081 | 0.7336 
| 4 | Step 3 + STOPWORDS + C=0.4 | 0.7957 | 0.8617 | 0.9070 | 0.7325 
| 5 | Step 3 + STOPWORDS + C=0.04 | 0.8078 | 0.8646 | 0.9083 | 0.7383 
| 6 | Step 6 + regExp | 0.8078 | 0.8638 | 0.9071 | 0.7379 

STOPWORDS = 'a','an','by','did','does', 'was', 'were', 'i'  



#### Train/Test stages for MIX:

| Step | Preprocess | val_acc on MIX(RT+IMDB) | val_acc on RT | val_acc on IMDB
| ------------- |:------------------ | :-----:|:--------:|:----|:--------:
| 7 | Step 6 | 0.8365 | 0.8078 | 0.9071