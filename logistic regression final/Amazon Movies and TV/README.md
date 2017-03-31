### Results on the same domain ### 

Data size | Amazon train <br/> 
Validation| Amazon test <br/>
Acc| Amazon test <br/>
F1 | Movie reviews <br/>
Acc | Movie reviews <br/>
F1| Amazon test <br/>
F1_neg| Movie reviews <br/>
F1_neg
:-------:|:------:|:--:|:--:|:--:|:--:|:--:|:--:|          
100K|0.941|0.938|0.940|0.617|0.560|0.785|0.420|
200K|0.949|0.939|0.940|0.649|0.610|0.709|0.396|
500K|0.939|0.939|0.942|0.650|0.610|0.747|0.490|
1000K|0.938|0.940|0.940|0.667|0.640|0.760|0.546|
All|0.939|0.941|0.940|0.675|0.670|0.763|0.555|
380K (balanced data)|0.89|0.899|0.900|0.750|0.740|0.752|0.567|

---

### Results on another domains ###  
Model Parameters: Hashing Vectorizer, n_gram range = (1, 3), reg exp, stop words from Snowball Stemmer, train set is balanced.
<br/>F1 score was calculated for negative reviews (` f1_score(pos_label = 0)`)

|  Domain | Test Accuracy | F1 score|
 --------|:-----:|:----:|
| Digital music|0.895|0.620|
 | Office products| 0.747|0.585|
 |Video games|0.840|0.606|
