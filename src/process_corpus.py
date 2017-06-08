from __future__ import print_function

import logging
import os.path
import six
import sys

from gensim.models.word2vec import LineSentence

if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))

    # check and process input arguments
    if len(sys.argv) != 2:
        print("Using: python process_corpus.py xxx.csv")
        sys.exit(1)

    inputfile = sys.argv[1]
    outputfile = sys.argv[1] + ".processed"
    space = " "
    i = 0

    output = open(outputfile, 'w')
    sentences = LineSentence(inputfile)
    
    for text in sentences:
        if six.PY3:
            output.write(u' '.join(text) + '\n')
        else:
            output.write(space.join(text) + "\n")
        i = i + 1
        if (i % 10000 == 0):
            logger.info("Saved " + str(i) + " articles")

    output.close()
    logger.info("Finished Saved " + str(i) + " articles in " + outputfile)