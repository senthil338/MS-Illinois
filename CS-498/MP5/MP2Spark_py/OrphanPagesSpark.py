#!/usr/bin/env python
import sys
from pyspark import SparkConf, SparkContext

class Count:
  def __init__(self, id, flag):
    self.id = id
    self.flag = flag

conf = SparkConf().setMaster("local").setAppName("OrphanPages")
conf.set("spark.driver.bindAddress", "127.0.0.1")
sc = SparkContext(conf = conf)


lines = sc.textFile(sys.argv[1], 1) 

res_link = []
res_link_1 = []
orphan_res = []  
ids = []

'''
for line in lines:
    line = line.strip()
    id, links_str = line.split(':')
    links = links_str.split()
    if links:
        res_link_1.append((id, 1))
        for link in links:
            res_link_1.append((link, 0))
'''

def mpfn(line):
#for line in lines:
    line = line.strip()
    res = line.split(':')
    id = res[0]
    print(id)
    links_str = res[1]
    links = links_str.split()
    if links:
        res_link_1.append((id, 1))
        print((id, 1))
        for link in links:
            res_link_1.append((link, 0))
            #print((link, 1))
    return res_link_1
   
def unicode_to_clean_str(x):
    converted = x.encode('utf-8')
    converted_1 = converted.split(':')
    result = []
    ids = converted_1[0].split()
    links = converted_1[1].split()
    print("Senthil")
    print(len(ids))
    for i in range(len(ids)):
        cnt = Count(ids[i],0)
        result.append(cnt)
    for i in range(len(links)):
        cnt = Count(links[i],1)
        result.append(cnt)
    return  result


one_RDD = lines.flatMap(lambda x: unicode_to_clean_str(x))
#one_RDD = lines.flatMap(lambda x: x.encode('utf-8'))
#one_RDD = one_RDD.map(lambda x: (x,0))
#one_RDD = lines.flatMap(lambda x: x.split(' '))
#one_RDD = lines.flatMap(lambda x: x.split(':'))
#one_RDD = one_RDD.filter(lambda x: len(x) )
one_RDD = one_RDD.map(lambda x: (x.id,1,x.flag))
one_RDD = one_RDD.reduceByKey(lambda x,y: x+y)
one_RDD = one_RDD.map(lambda x: (int(x[0].id),int(x[1])))
one_RDD = one_RDD.filter(lambda x: x[1].flag==1)
result = one_RDD.sortByKey(False).keys().collect()
#result = one_RDD.sortByKey(False).take(10)

#TODO
#result.sort()

output = open(sys.argv[2], "w")



#TODO
#write results to output file. Foramt for each line: (line+"\n")

sc.stop()

