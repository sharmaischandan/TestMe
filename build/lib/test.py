from pyspark import SparkContext

import os
os.environ['SPARK_HOME']="D:/spark"
sc = SparkContext(appName="TestApp")
textdata = sc.textFile("D:\spark\README.md")

counts = textdata.flatMap(lambda x: x.split(' ')) \
                  .map(lambda x: (x, 1)) \
                  .reduceByKey(lambda x,y : x+y).sortBy(lambda x: x[1], ascending=False)
output = counts.collect()
for (word, count) in output: print "%s: %i" % (word, count)

sc.stop()