Mean and Standard Deviation by Spark's combineByKey()
=====================================================

````
# ./bin/pyspark
Python 2.7.10 (default, Oct 23 2015, 19:19:21)
...
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /__ / .__/\_,_/_/ /_/\_\   version 1.6.1
      /_/

Using Python version 2.7.10 (default, Oct 23 2015 19:19:21)
SparkContext available as sc, HiveContext available as sqlContext.
>>> data = [
...         ("A", 2.), ("A", 4.), ("A", 9.),
...         ("B", 10.), ("B", 20.),
...         ("Z", 3.), ("Z", 5.), ("Z", 8.), ("Z", 12.)
...        ]
>>> data
[
 ('A', 2.0), 
 ('A', 4.0), 
 ('A', 9.0), 
 ('B', 10.0), 
 ('B', 20.0), 
 ('Z', 3.0),
 ('Z', 5.0), 
 ('Z', 8.0), 
 ('Z', 12.0)
]
>>> rdd = sc.parallelize( data )
>>> rdd.collect()
[
 ('A', 2.0), 
 ('A', 4.0), 
 ('A', 9.0), 
 ('B', 10.0), 
 ('B', 20.0), 
 ('Z', 3.0), 
 ('Z', 5.0), 
 ('Z', 8.0), 
 ('Z', 12.0)
]
>>> rdd.count()
9
>>> sumCount = rdd.combineByKey(lambda value: (value, value*value, 1),
...                             lambda x, value: (x[0] + value, x[1] + value*value, x[2] + 1),
...                             lambda x, y: (x[0] + y[0], x[1] + y[1], x[2] + y[2])
...                            )

>>> sumCount.collect()
[
 ('A', (15.0, 101.0, 3)), 
 ('Z', (28.0, 242.0, 4)), 
 ('B', (30.0, 500.0, 2))
]

>>> import math
>>> def  stdDev( sumX, sumSquared, n ):
...     mean = sumX / n
...     stdDeviation = math.sqrt ((sumSquared - n*mean*mean) /n)
...     return (mean, stdDeviation)
... ^D

>>> meanAndStdDev = sumCount.mapValues(lambda x : stdDev(x[0], x[1], x[2]))
>>> meanAndStdDev.collect()
[
 ('A', (5.0, 2.943920288775949)), 
 ('Z', (7.0, 3.391164991562634)), 
 ('B', (15.0, 5.0))
]
>>>
````