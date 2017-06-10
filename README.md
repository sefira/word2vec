# word2vec 一个中文word2vec
This is my word2vec for douban reviews
在豆瓣电影影评上进行word2vec

## Install
 - Install gcc by `sudo apt-get install gcc` before install Anaconda and gensim, otherwise gensim will run in slow verison(70x slower).
 - Install Anaconda
 - Install gensim

## Process Corpus
 - cd src
 - Pre-process corpus (maybe not necessary, but just follow the [使用 word2vec 训练wiki中英文语料库](http://www.jianshu.com/p/05800a28c5e4))
   - input: onlyreview_douban_movie.tsv is a file in which a douban review lays on one line.
   - output: onlyreview_douban_movie.tsv.processed in which a processed douban review lays on one line.
   - pre-process: `python process_corpus.py ../data/onlyreview_douban_movie.tsv`

 - Traditional Chinese to Simple Chinese
   - Install opencc `sudo apt-get install opencc`
   - Trans `opencc -i ../data/onlyreview_douban_movie.tsv.processed -o ../data/onlyreview_douban_movie.tsv.processed.simpleCh -c zht2zhs.ini`

 - Word Break
   - Install jieba `pip install jieba`
   - Word break: `python word_breaker.py ../data/onlyreview_douban_movie.tsv.processed.simpleCh`

 - Remove words
   - Remove words: `python remove_words.py ../data/onlyreview_douban_movie.tsv.processed.simpleCh.wordbreak`

 - Train Word2Vec
   - `python train_word2vec.py -train ../data/onlyreview_douban_movie.tsv.processed.simpleCh.wordbreak.removeword` or `python train_word2vec.py -train ../data/onlyreview_douban_movie.tsv.processed.simpleCh.wordbreak.removeword -size 300 -window 5 -sg 1 -min_count 100 -negative 10 -iter 25 -workers 12
`
 
 - Evaluate Word2Vec
   - `python test_word2vec.py ../data/xxx.model`

 - Resume Training
   - `python resume_train.py -finetune ../model/onlyreview_douban_movie.tsv.processed.simpleCh.wordbreak.removewordsize300window5sg1min_count100negative10iter25.model -train ../data/onlyreview_douban_movie.tsv.processed.simpleCh.wordbreak.removeword`
 