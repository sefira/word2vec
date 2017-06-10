import logging
import os
import sys
import multiprocessing
import argparse

from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence

if __name__ == '__main__':
    # check and process input arguments
    if len(sys.argv) < 2:
        print(globals()['__doc__'] % locals())
        print("Using: python resume_train.py -finetune xxx.model -train xxx.tsv")
        sys.exit(1)

    parser = argparse.ArgumentParser()
    parser.add_argument("-finetune", required=True, help="Fine tune some model")
    parser.add_argument("-train", required=True, help="Use text data from file TRAIN to train the model")
    args = parser.parse_args()

    outputpath = "../model/"
    inpputfile = args.train
    outputfile1 = outputpath + args.finetune + ".model"
    outputfile2 = outputpath + args.finetune + ".vector"

    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)
    logging.basicConfig(filename='finetune'+args.finetune.split("/")[-1]+'.log', 
                        filemode='w', 
                        format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))

    model = Word2Vec.load(args.finetune)
    model.train(LineSentence(inpputfile), 
        total_examples=model.corpus_count, 
        epochs=model.iter)

    model.save(outputfile1)
    model.wv.save_word2vec_format(outputfile2, binary=False)
    logger.info("Saved model in " + outputfile1)
    logger.info("Saved vector in " + outputfile2)


    questionfile = "../data/questions-words-Zh.txt"
    model.accuracy(questionfile)