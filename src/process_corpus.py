import logging
import os.path
import sys
import jieba
import re

#################### config ###################
path = "../data/"
# data = "test_corpus.csv"
# data = "review_douban_movie.tsv"
# data = "review_douban_movie.tsv"
data = "zhidao_dataneg.tsv"
############### end of config #################

logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
logging.root.setLevel(level=logging.INFO)
logger = logging.getLogger()

def Tradition2Simple():
    logger.info("running Tradition to Simple in " + path + data)

    inputfile = path + data
    outputfile = path + data + ".zhs"
    cmd = "opencc -i " + inputfile + " -o " + outputfile + " -c zht2zhs.ini"
    os.system(cmd)

def WordBeark():
    logger.info("running Word Beark in " + path + data)

    inputfile = path + data + ".zhs"
    outputfile = path + data + ".wordbreak"
    i = 0
    output = open(outputfile, 'w')
    input = open(inputfile, 'r')

    for line in input.readlines():
        seg_list = jieba.cut(line)
        output.write(u' '.join(seg_list))

        i = i + 1
        if (i % 10000 == 0):
            logger.info("Cut " + str(i) + " articles")

    output.close()
    logger.info("Finished Saved " + str(i) + " articles in " + outputfile)

def RemoveWord():
    logger.info("running Remove Word in " + path + data)

    inputfile = path + data + ".wordbreak"
    outputfile = path + data + ".removeword"
    i = 0
    output = open(outputfile, 'w')
    input = open(inputfile, 'r')

    for line in input.readlines():
        if(len(line) < 2):
            continue
        ss = re.findall('[\n\s*\r\u4e00-\u9fa5]|nmovie|nrcelebrity', line)
        output.write("".join(ss).strip() + '\n')

        i = i + 1
        if (i % 10000 == 0):
            logger.info("remove words " + str(i) + " articles")

    output.close()
    logger.info("Finished Saved " + str(i) + " articles in " + outputfile)

def CountMaxLength():
    inputfile = path + data + ".removeword"
    input = open(inputfile, "r")
    length = 0
    for line in input.readlines():
        #line = line.decode("utf-8")
        line = line.split()
        length=max(len(line),length)
    return length

#Tradition2Simple()
#WordBeark()
#RemoveWord()

length = CountMaxLength()
print("Max length of these sentense is " + str(length))