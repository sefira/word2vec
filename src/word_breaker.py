import os
import logging
import sys
import six
import jieba

if __name__=='__main__':

    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))

    if len(sys.argv) != 2:
        print("Using: python word_breaker.py xxx.tsv")
        sys.exit(1)

    inputfile = sys.argv[1]
    outputfile = sys.argv[1] + ".wordbreak"
    space = " "
    i = 0
    
    output = open(outputfile, 'w')
    input = open(inputfile, 'r')

    for line in input.readlines():
        seg_list = jieba.cut(line)
        if six.PY3:
            output.write(u' '.join(seg_list))
        else:
            output.write(space.join(seg_list))
        i = i + 1
        if (i % 10000 == 0):
            logger.info("Cut " + str(i) + " articles")

    output.close()
    logger.info("Finished Saved " + str(i) + " articles in " + outputfile)