import logging
import os
import sys
import multiprocessing
from gensim.models import Word2Vec

#################### config ###################
modelfile = "../model/size300window5sg1min_count100negative10iter50.model"
questionfile = "../data/questions-words-Zh.txt"
############### end of config #################

logger = logging.getLogger()
logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
logging.root.setLevel(level=logging.INFO)
logger.info("running test word2vec for model: %s" % modelfile)

model = Word2Vec.load(modelfile)
acc = model.accuracy(questionfile)
positive = len(acc[-1]["correct"])
negitive = len(acc[-1]["incorrect"])

logger.info("Test model " + modelfile + " in " + questionfile)