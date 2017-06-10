import logging
import os.path
import six
import sys
import jieba

if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))

    # check and process input arguments
    if len(sys.argv) != 2:
        print("Using: python process_corpus.py xxx.tsv")
        sys.exit(1)

    inputfile = sys.argv[1]
    outputfile = sys.argv[1] + ".processed"
    space = " "
    i = 0

    output = open(outputfile, 'w')
    input = open(inputfile, "r")
    
    for line in input.readlines():
        if six.PY3:
            data = line.split("\t")
            question = data[0]
            question = question.replace("<nmovie>", "nmovie")
            question = question.replace("<nrcelebrity>", "nrcelebrity")
            seg_list = jieba.cut(question)
            output.write(u' '.join(seg_list) + "\n")

        i = i + 1
        if (i % 10000 == 0):
            logger.info("Saved " + str(i) + " questions")

    output.close()
    logger.info("Finished Saved " + str(i) + " questions in " + outputfile)