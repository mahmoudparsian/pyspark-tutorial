from __future__ import print_function

import sys

from pyspark.sql import SparkSession
#-----------------------------------


if __name__ == "__main__":

    # create an instance of a SparkSession as spark
    spark = SparkSession\
        .builder\
        .appName("wordcount")\
        .getOrCreate()

    inputPath = "file:///Users/mparsian/spark-2.2.1/zbin/sample.txt"

    # create SparkContext as sc
    sc = spark.sparkContext

    # create RDD from a text file
    textfileRDD = sc.textFile(inputPath)
    print(textfileRDD.collect())

    wordsRDD = textfileRDD.flatMap(lambda line: line.split(" "))
    print(wordsRDD.collect())

    pairsRDD =  wordsRDD.map(lambda word: (word, 1))
    print(pairsRDD.collect())

    frequenciesRDD = pairsRDD.reduceByKey(lambda a, b: a + b)
    print(frequenciesRDD.collect())

    # done!
    spark.stop()
