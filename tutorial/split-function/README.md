How To Use Split Function
=========================

* Example-1: Split ````RDD<String>```` into Tokens

````
# ./bin/pyspark
Python 2.7.10 (default, Oct 23 2015, 19:19:21)

Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /__ / .__/\_,_/_/ /_/\_\   version 1.6.1
      /_/

Using Python version 2.7.10 (default, Oct 23 2015 19:19:21)
SparkContext available as sc, HiveContext available as sqlContext.

>>> data = ["abc,de", "abc,de,ze", "abc,de,ze,pe"]
>>> data
['abc,de', 'abc,de,ze', 'abc,de,ze,pe']

>>> rdd = sc.parallelize(data)
>>> rdd.collect()
['abc,de', 'abc,de,ze', 'abc,de,ze,pe']
>>> rdd.count()
3

>>> rdd2 = rdd.flatMap(lambda x : x.split(","))
>>> rdd2.collect()
['abc', 'de', 'abc', 'de', 'ze', 'abc', 'de', 'ze', 'pe']
>>> rdd2.count()
9
````

* Example-2: Create Key-Value Pairs

````
>>> data2 = ["abc,de", "xyz,deeee,ze", "abc,de,ze,pe", "xyz,bababa"]
>>> data2
['abc,de', 'xyz,deeee,ze', 'abc,de,ze,pe', 'xyz,bababa']

>>> rdd4 = sc.parallelize(data2)
>>> rdd4.collect()
['abc,de', 'xyz,deeee,ze', 'abc,de,ze,pe', 'xyz,bababa']

>>> rdd5 = rdd4.map(lambda x : (x.split(",")[0], x.split(",")[1]))
>>> rdd5.collect()
[('abc', 'de'), ('xyz', 'deeee'), ('abc', 'de'), ('xyz', 'bababa')]
````
