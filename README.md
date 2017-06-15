# word2vec 一个中文word2vec
This is a word2vec for Chinese douban movie reviews
在豆瓣电影影评上进行word2vec, 一个中文语料word2vec

***

## Install
 - Install gcc by `sudo apt-get install gcc` before install Anaconda and gensim, otherwise gensim will run in slow verison(70x slower).
 - Install Anaconda
 - Install gensim

## Process Corpus
 - Going to src/ `cd src`
 - Execute process_corpus.py `python -i process_corpus.py`
   - input: review_douban_movie.tsv is a file in which a douban review lays on one line.
   - output: review_douban_movie.tsv.removeword in which a processed douban review lays on one line. Some dependents should be installed for those process flow.

   - Tradition2Simple
     - Install opencc `sudo apt-get install opencc`

   - WordBeark
     - Install jieba `pip install jieba`

   - RemoveWord

   - Then we maybe cat some files together if we split corpus into several files, using `cat file1 file2 > file3` or `cat file2 >> file1`

## Train Word2Vec
 - Going to src/ `cd src`
 - Execute train_word2vec.py `python -i train_word2vec.py -size 300 -window 5 -sg 1 -min_count 100 -negative 10 -iter 25 -workers 12`

## Evaluate Word2Vec
 - Going to src/ `cd src`
 - Execute test_word2vec.py `python -i test_word2vec.py ../data/xxx.model`
 - questions-words-Zh.txt is a Chinese evaluation file translated from English questions-words.txt using Microsoft Bing Translator API.

## Finetune Training
 - `python -i finetune.py -finetune ../model/review_douban_movie.tsv.removewordsize300window5sg1min_count100negative10iter25.model -train ../data/wv_train.data`

## Some usages in gensim Word2Vec
 - Get the vector of a word: model.wv["word"], i.e. model.wv["apple"]
 - Get the index of a word: model.wv.vocab["word"].index, i.e. model.wv.vocab["apple"].index
 - Get a word by its index: model.wv.index2word[index], i.e. model.wv.index2word[5585]
 - Find the most similar word of a given word: model.wv.most_similar("word"), i.e. model.wv.most_similar("apple")
 - Evaluate a model on analogies: model.wv.accuracy( 'questions-words.txt')

***

## 安装
 - 确保安装gcc，否则根据官网的说法word2vec会慢70倍。使用命令`sudo apt-get install gcc`
 - 安装Anaconda
 - 安装gensim

## 处理语料
 - 进入src文件夹
 - 执行process_corpus.py, `python -i process_corpus.py`
   - 其中输入为review_douban_movie.tsv，每一行有一条豆瓣影评，一共65w行
   - 输出为review_douban_movie.tsv.removeword，每一行都被繁体转简体、分词、去除标点
   
   - 繁体转简体
     - 安装opencc `sudo apt-get install opencc`

   - 分词
     - 安装jieba `pip install jieba`

   - 去除标点

   - 如果多个语料文件分开处理，最后我们可以使用Linux的cat将他们连在一起，如 `cat file1 file2 > file3`或`cat file2 >> file1`

## 训练Word2Vec
 - 进入src文件夹
 - 执行train_word2vec.py `python -i train_word2vec.py -size 300 -window 5 -sg 1 -min_count 100 -negative 10 -iter 25 -workers 12`

## 评估Word2Vec
 - 进入src文件夹
 - 执行test_word2vec.py `python -i test_word2vec.py ../data/xxx.model`
 - 值得一提的是，在这一步中我贡献了中文word2vec领域第一份评估标准：data/questions-words-Zh.txt，该标准是英文版的analogies任务翻译为中文。是我在Microsoft期间使用Bing Translator API翻译，翻译质量上乘。一些例子：

|a|b|c|d|
| ------ | ------ | ------ | ------ |
|写|写作|读|阅读|
|写|写作|慢|放缓|
|想|思考|唱|唱歌|
|大|最大|小|最小|
|好|最好|高|最高|
|侄子|侄女|王子|公主|
|侄子|侄女|儿子|女儿|
|雅典|希腊|曼谷|泰国|
|雅典|希腊|北京|中国|

## Finetune训练
 - `python -i finetune.py -finetune ../model/review_douban_movie.tsv.removewordsize300window5sg1min_count100negative10iter25.model -train ../data/wv_train.data`

## 一些gensim Word2Vec的使用方法
 - 获取词向量: model.wv["word"], i.e. model.wv["刘德华"]
 - 获取词索引index: model.wv.vocab["word"].index, i.e. model.wv.vocab["张艺谋"].index
 - 通过index获取词: model.wv.index2word[index], i.e. model.wv.index2word[5585]
 - 找一个词最相近的词: model.wv.most_similar("word"), i.e. model.wv.most_similar("周星驰")
 - 四词类推评价: model.wv.accuracy( 'questions-words.txt')
