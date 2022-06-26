Problem: Given a set of (K, V) pairs,
find (sum, count, min, max) per key using 
the combineByKey() transformation.

~/spark-2.4.4 $ ./bin/pyspark
Python 3.7.2 (v3.7.2:9a3ffc0492, Dec 24 2018, 02:44:43)
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /__ / .__/\_,_/_/ /_/\_\   version 2.4.4
      /_/

Using Python version 3.7.2 (v3.7.2:9a3ffc0492, Dec 24 2018 02:44:43)
SparkSession available as 'spark'.
>>>

>>>
>>> spark
<pyspark.sql.session.SparkSession object at 0x119f71668>
>>> data = [('A', 2), ('A', 3), ('A', 4), ('A', 5), ('B', 6), ('B', 7), ('B', 8) ]
>>> data
[('A', 2), ('A', 3), ('A', 4), ('A', 5), ('B', 6), ('B', 7), ('B', 8)]
>>> rdd = spark.sparkContext.parallelize(data)
>>>
>>>
>>> rdd.count()
7
>>> rdd.collect()
[('A', 2), ('A', 3), ('A', 4), ('A', 5), ('B', 6), ('B', 7), ('B', 8)]
>>> # (K, (sum, count, min, max))
...
>>> def single(v):
...    return (v, 1, v, v)
...
>>> def merge(C, v):
...    return (C[0]+v, C[1]+1, min(C[2],v), max(C[3],v))
...
>>> def combine(C1, C2):
...    return (C1[0]+C2[0], C1[1]+C2[1], min(C1[2], C2[2]), max(C1[3], C2[3]) )
...
>>> rdd2 = rdd.combineByKey(single, merge, combine)
>>> rdd2.collect()
[
 ('B', (21, 3, 6, 8)), 
 ('A', (14, 4, 2, 5))
]

