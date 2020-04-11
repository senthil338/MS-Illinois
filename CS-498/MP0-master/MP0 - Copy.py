#! python2
import random 
import os
import string
import sys
import re
import operator
from collections import OrderedDict

stopWordsList = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours",
            "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its",
            "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that",
            "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having",
            "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
            "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
            "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
            "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
            "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
            "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

delimiters = " \t,;.?!-:@[](){}_*/"

def split(delimiters, string, maxsplit=0):
    import re
    regexPattern = '|'.join(map(re.escape, delimiters))
    return re.split(regexPattern, string)

def getIndexes(seed):
    random.seed(seed)
    n = 10000
    number_of_lines = 50000
    ret = []
    for i in range(0,n):
        ret.append(random.randint(0, 50000-1))
    return ret


def split_to_words(sentences):
    word_list = []
    writefile(sentences)
    for sentence in sentences:
        for word in split(delimiters,sentence):
            for stop in stopWordsList:
                word = word.replace(stop,'')
                if word and word.lower().strip() not in stopWordsList and word.strip() != '':
                    word_list.append(word.lower().strip())
    return word_list

def writefile(param):
     with open('C:\Senthil\Masters\CS 498 CCA\MP0-master\MP0-master\listfile.txt', 'w') as filehandle:
        for listitem in param:
            filehandle.write('%s\n' % listitem)

def process(userID):
    indexes = getIndexes(userID)

    print(len(indexes))
    #indexes = userID
    ret = []
    # TODO
    # read in txt
    superlines = []
    sublines = []
    #filepath = 'c:\Senthil\Masters\CS 498 CCA\MP0-master\MP0-master\input.txt'
    #with open(filepath) as fp:
    for index, line in enumerate(sys.stdin.readlines()):
        #if index in indexes:
        superlines.append(line)
                    #print("Line {}: {}".format(index, line))
    print len(superlines)
    for index in indexes:
        if superlines[index]:
            sublines.append(superlines[index])
    print len(sublines)
    #print len(sublines)
    word_list = split_to_words(sublines)
    print len(word_list)
    
    # dict counter
    counts = dict()
    for w in word_list:
        counts[w] = counts.get(w, 0) + 1
   
  	# sort by desc value then asc key
    sorted_count = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    # 1 sorted_count = list(sorted(counts.items(), key = lambda i : (i[1],i[0]), reverse = True))
   
    #sorted_count = sorted(counts.items(), key=operator.itemgetter(1),reverse=True)[0:30]
    #print sorted_count
  	# first element to list ret
    
    ret = [word[0] for word in sorted_count[0:20]] 
    for word in ret:
        print(word)
        
        

process(sys.argv[1])
#process(0)
