#!/usr/bin/env python
import sys
from pyspark import SparkConf, SparkContext
import math

conf = SparkConf().setMaster("local").setAppName("TopTitleStatistics")
conf.set("spark.driver.bindAddress", "127.0.0.1")
sc = SparkContext(conf = conf)

lines = sc.textFile(sys.argv[1],1)
result = lines.sortByKey(False).take(10)
#TODO
counts = []
for line in result:
    line = line.strip().split(' ')
    count = int(line[1])
    counts.append(count)

mean = math.floor(sum(counts) / len(counts))
var = math.floor(sum([(x-mean)**2 for x in counts]) / len(counts))

outputFile = open(sys.argv[2],"w")
'''
TODO write your output here
write results to output file. Format
'''
outputFile.write('Mean\t%s\n' % mean)
outputFile.write('Sum\t%s\n' % sum(counts))
outputFile.write('Min\t%s\n' % min(counts))
outputFile.write('Max\t%s\n' % max(counts))
outputFile.write('Var\t%s\n' % var)


sc.stop()

