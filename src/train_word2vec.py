import logging
import os
import sys
import multiprocessing
import argparse
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence

#################### config ###################
#data = "../data/review_douban_movie.tsv.removeword"
#data = "../data/test_corpus.csv.removeword"
#data = "../data/zhidao_dataneg.tsv.removeword"
data = "../data/wv_train.data"
parser = argparse.ArgumentParser()
parser.add_argument("-train",       type=str, default=data, help="Use text data from file TRAIN to train the model")
parser.add_argument("-size",        type=int, default=300,  help="Set size of word vectors; default is 100")
parser.add_argument("-window",      type=int, default=5,    help="Set max skip length WINDOW between words; default is 5")
parser.add_argument("-sg",          type=int, default=1,    choices=[0, 1], help="By default (sg=0), CBOW is used. Otherwise (sg=1), skip-gram is employed.")
parser.add_argument("-min_count",   type=int, default=100,  help="This will discard words that appear less than MIN_COUNT times; default is 5")
parser.add_argument("-negative",    type=int, default=10,   help="Number of negative examples; default is 5, common values are 3 - 10 (0 = not used)")
parser.add_argument("-workers",     type=int, default=12,   help="Use THREADS threads (default 12)")
parser.add_argument("-sample",      type=float,default=1e-3,help="Set threshold for occurrence of words. Those that appear with higher frequency in the training data will be randomly down-sampled; default is 1e-3, useful range is (0, 1e-5)")
parser.add_argument("-hs",          type=int, default=0,    choices=[0, 1], help="Use Hierarchical Softmax; default is 0 (not used)")
parser.add_argument("-iter",        type=int, default=25,   help="Run more training iterations (default 5)")
args = parser.parse_args()

outputpath = "../model/"
inpputfile = args.train
config_pattern = "size{}window{}sg{}min_count{}negative{}iter{}"
config_str = config_pattern.format(
    args.size, 
    args.window, 
    args.sg, 
    args.min_count, 
    args.negative, 
    args.iter
    )
outputfile1 = outputpath + config_str + ".model"
outputfile2 = outputpath + config_str + ".vector"
############### end of config #################

logging.basicConfig(filename=config_str+'.log', 
                    filemode='w', 
                    format='%(asctime)s: %(levelname)s: %(message)s'
                    )
logging.root.setLevel(level=logging.INFO)
logger = logging.getLogger()
logger.info("running train process in data: %s" % args.train)


model = Word2Vec(LineSentence(inpputfile), 
    size=args.size, 
    window=args.window, 
    min_count=args.min_count,   # with 0.35 billion corpus, #3000 can retain 9228 unique words
    workers=args.workers,       # multiprocessing.cpu_count()
    #sample=args.sample,
    sg=args.sg,
    #hs=args.hs,
    negative=args.negative,     # follow tensorflow's word2vec_optimized.py num_neg_samples 25
    iter=args.iter
    )

# trim unneeded model memory = use(much) less RAM
# model.init_sims(replace=True)
model.save(outputfile1)
model.wv.save_word2vec_format(outputfile2, binary=False)
logger.info("Saved model in " + outputfile1)
logger.info("Saved vector in " + outputfile2)

# test word2vec
questionfile = "../data/questions-words-Zh.txt"
model.accuracy(questionfile)