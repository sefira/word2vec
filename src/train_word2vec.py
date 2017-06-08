import logging
import os
import sys
import multiprocessing

from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence

if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))

    # check and process input arguments
    if len(sys.argv) != 2:
        print("Using: python train_word2vec.py xxx.tsv")
        sys.exit(1)

    outputpath = "../model/"
    inpputfile = sys.argv[1]
    outputfile1 = outputpath + sys.argv[1].split('/')[-1] + ".model"
    outputfile2 = outputpath + sys.argv[1].split('/')[-1] + ".vector"

    model = Word2Vec(LineSentence(inpputfile), 
        size=200, 
        window=5, 
        min_count=50,
        #max_vocab_size=None, 
        workers=multiprocessing.cpu_count(),
        #sample=args.sample,
        sg=1,
        #hs=args.hs,
        negative=25,    # follow tensorflow's word2vec_optimized.py num_neg_samples
        iter=15
        )

    # trim unneeded model memory = use(much) less RAM
    # model.init_sims(replace=True)
    model.save(outputfile1)
    model.wv.save_word2vec_format(outputfile2, binary=False)
    logger.info("Saved model in " + outputfile1)
    logger.info("Saved vector in " + outputfile2)