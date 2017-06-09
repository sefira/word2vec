import logging
import os
import sys
import multiprocessing

from gensim.models import Word2Vec

if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))

    # check and process input arguments
    if len(sys.argv) != 2:
        print("Using: python test_word2vec.py xxx.model")
        sys.exit(1)

    modelfile = sys.argv[1]
    questionfile = "../data/questions-words-Zh.txt"

    model = Word2Vec.load(modelfile)
    acc = model.accuracy(questionfile)
    positive = len(acc[-1]["correct"])
    negitive = len(acc[-1]["incorrect"])

    logger.info("Test model " + modelfile + " in " + questionfile)