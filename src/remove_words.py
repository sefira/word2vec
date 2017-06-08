import os
import logging
import sys
import six
import jieba
import re

if __name__=='__main__':

    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))

    if len(sys.argv) != 2:
        print("Using: python remove_words.py xxx.tsv")
        sys.exit(1)

    inputfile = sys.argv[1]
    outputfile = sys.argv[1] + ".removeword"
    space = " "
    i = 0
    
    output = open(outputfile, 'w')
    input = open(inputfile, 'r')

    for line in input.readlines():
        if(len(line) < 2):
            continue
        ss = re.findall('[\n\s*\r\u4e00-\u9fa5]', line)
        output.write("".join(ss).strip() + '\n')

        i = i + 1
        if (i % 10000 == 0):
            logger.info("remove words " + str(i) + " articles")

    output.close()
    logger.info("Finished Saved " + str(i) + " articles in " + outputfile)