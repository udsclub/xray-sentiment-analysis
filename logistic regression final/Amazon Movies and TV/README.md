### Results on the same domain ### 

Data size | Amazon train <br/> 
Validation| Amazon test <br/>
Acc| Amazon test <br/>
F1 | Movie reviews <br/>
Acc | Movie reviews <br/>
F1
:-------:|:------:|:--:|:--:|:--:|:--:|           
100K|0.941|0.938|0.94|0.617|0.56|
200K|0.949|0.939|0.94|0.649|0.61|
500K|0939|0.939|0.942|0.65|0.61|
1000K|093.8|0.940|0.94|0.667|0.64|
All|0.939|0.941|0.94|0.675|0.67|
380K (balanced data)|0.89|0.899|0.9|0.75|0.74

---

### Results on another domains ###  
Model Parameters: Hashing Vectorizer, n_gram range = (1, 3), reg exp, stop words from Snowball Stemmer, train set is balanced.
<br/>F1 score was calculated for negative reviews (` f1_score(pos_label = 0)`)

|  Domain | Test Accuracy | F1 score|
 --------|:-----:|:----:|
| Digital music|0.895|0.620|
 | Office products| 0.747|0.285|
 |Video games|0.840|0.606|
