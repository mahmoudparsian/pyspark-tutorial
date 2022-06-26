from __future__ import print_function

import sys

from pyspark.sql import SparkSession

#
print ("This is the name of the script: ", sys.argv[0])
print ("Number of arguments: ", len(sys.argv))
print ("The arguments are: " , str(sys.argv))
#

#   DEFINE your input path
input_path = sys.argv[1]
print("input_path: ", input_path)


#   CREATE an instance of a SparkSession object
spark = SparkSession\
    .builder\
    .appName("PythonWordCount")\
    .getOrCreate()

#   CREATE a new RDD[String]
#lines = spark.sparkContext.textFile(input_path)
# APPLY a SET of TRANSFORMATIONS...

#-------------------------------------------
def minmax(partition):
	first_time = False
	#count
	#min2
	#max2
	for x in partition:
		if (first_time == False):
			count = 1
			min2 = x
			max2 = x
			first_time = True
		else:
			count = count + 1
			max2 = max(x, max2)
			min2 = min(x, min2)
	#end-for
	#
	return [(count, min2, max2)]
#end-def
#---------------------
def iterate_partition(partition):
   elements = []
   for x in partition:
      elements.append(x)
   print("elements=", elements)
   #print ("==================")
#end-def
#-------------------------
def add3(t1, t2):
	count = t1[0] + t2[0]
	min2 = min(t1[1], t2[1])
	max2 = max(t1[2], t2[2])
	return (count, min2, max2)
#end-def

data = [10, 20, 30, 44, 55, 3, 4, 60, 50, 5, 2, 2, 20, 20, 10, 30, 70]
print("data=", data)
print("==============")

#
rdd = spark.sparkContext.parallelize(data, 4)
print("rdd.collect()=", rdd.collect())
print("==============")
#
rdd.foreachPartition(iterate_partition)
print("==============")
#

count_min_max_rdd = rdd.mapPartitions(minmax)
print("minmax_rdd.collect()=", count_min_max_rdd.collect())

final_triplet = count_min_max_rdd.reduce(add3)
print("final_triplet=", final_triplet)

spark.stop()
