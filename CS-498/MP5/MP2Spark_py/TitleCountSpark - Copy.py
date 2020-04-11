#!/usr/bin/env python

'''Exectuion Command: spark-submit TitleCountSpark.py stopwords.txt delimiters.txt dataset/titles/ dataset/output'''

import sys
from pyspark import SparkConf, SparkContext
import re

stopWordsPath = sys.argv[1]
delimitersPath = sys.argv[2]
stop_words = ["","i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours",
            "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its",
            "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that",
            "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having",
            "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
            "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
            "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
            "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
            "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
            "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
delimiters = ""


with open(stopWordsPath) as f:
    read_data = f.readlines()
    #for x in read_data:
        #if x.strip() != "":
            #stop_words.append(x)

with open(delimitersPath) as f:
    delimiters = f.read()
result = []
def split(str):
    import re
    regexPattern = '|'.join(map(re.escape, delimiters))
    listofWords = re.split(regexPattern, str)
    #est_copy = {k: listofWords[k] for k in listofWords if k not in stopList}
    return listofWords
    

def unicode_to_clean_str(x):
    converted = x.encode('utf-8')
    lowercase_str = converted.lower()
    clear_str = split(lowercase_str)
    return  clear_str




conf = SparkConf().setMaster("local").setAppName("TitleCount")
conf.set("spark.driver.bindAddress", "127.0.0.1")
sc = SparkContext(conf = conf)

lines = sc.textFile(sys.argv[3],1)
one_RDD = lines.flatMap(lambda x: unicode_to_clean_str(x))
one_RDD = one_RDD.filter(lambda x: x.lower() not in stop_words)
one_RDD = one_RDD.map(lambda x: (x,1))
one_RDD = one_RDD.reduceByKey(lambda x,y: x+y)
one_RDD = one_RDD.map(lambda x: (x[1],x[0]))
#one_RDD = one_RDD.map(lambda x: (x[0],x[1]))
result = one_RDD.sortByKey(False).take(10)
#result = result.map(lambda x: (x[0],x[1]))
#sorted_count = sorted(result, key=lambda x: (-x[1], x[0]))

#TODO

outputFile = open(sys.argv[4],"w")
for i in range(len(result)):
     outputFile.write(str(result[i][1]) + " " + str(result[i][0]) +"\n")
outputFile.close()
#TODO

#write results to output file. Foramt for each line: (line +"\n")

sc.stop()
