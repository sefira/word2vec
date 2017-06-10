# word2vec 一个中文word2vec
This is my word2vec for douban reviews
在豆瓣电影影评上进行word2vec

## Install
 - Install gcc by `sudo apt-get install gcc` before install Anaconda and gensim, otherwise gensim will run in slow verison(70x slower).
 - Install Anaconda
 - Install gensim

## Process Corpus
 - Going to src/ `cd src`
 - Execute process_corpus.py `python -i process_corpus.py`
   - input: review_douban_movie.tsv is a file in which a douban review lays on one line.
   - output: review_douban_movie.tsv.removeword in which a processed douban review lays on one line.

   - Tradition2Simple
     - Install opencc `sudo apt-get install opencc`

   - WordBeark
     - Install jieba `pip install jieba`

   - RemoveWord

## Train Word2Vec
 - Going to src/ `cd src`
 - Execute train_word2vec.py `python -i train_word2vec.py -size 300 -window 5 -sg 1 -min_count 100 -negative 10 -iter 25 -workers 12`
 
## Evaluate Word2Vec
 - Going to src/ `cd src`
 - Execute test_word2vec.py `python -i test_word2vec.py ../data/xxx.model`

## Finetune Training
   - `python -i finetune.py -finetune ../model/review_douban_movie.tsv.removewordsize300window5sg1min_count100negative10iter25.model -train ../data/wv_train.data`
 