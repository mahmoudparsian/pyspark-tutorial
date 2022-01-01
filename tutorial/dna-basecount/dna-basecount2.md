DNA Base Counting using PySpark Using In-Mapper Combiner
========================================================

DNA Base Count Definition
-------------------------
[DNA Base Counting is defined here.](https://www.safaribooksonline.com/library/view/data-algorithms/9781491906170/ch24.html)

Solution in PySpark
-------------------
This solution assumes that each record is a DNA sequence. 
This solution uses "In-Mapper Combiner" design pattern 
and aggregates bases for each sequence before full
aggregation of all frequencies for unique bases.


````
$ cat /home/mparsian/dna_seq.txt
ATATCCCCGGGAT
ATCGATCGATAT


# ./bin/pyspark
Python 2.7.10 (default, Aug 22 2015, 20:33:39) 
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /__ / .__/\_,_/_/ /_/\_\   version 1.6.0
      /_/

SparkContext available as sc, HiveContext available as sqlContext.
>>> recs = sc.texFile('file:///home/mparsian/dna_seq.txt')

>>> recs.collect()
[
 u'ATATCCCCGGGAT', 
 u'ATCGATCGATAT'
]

>>> def mapper(seq):
...     freq = dict()
...     for x in list(seq):
...             if x in freq:
...                     freq[x] +=1
...             else:
...                     freq[x] = 1
...     #
...     kv = [(x, freq[x]) for x in freq]
...     return kv
... ^D


>>> rdd = recs.flatMap(mapper)
>>> rdd.collect()
[
 (u'A', 3), 
 (u'C', 4), 
 (u'T', 3), 
 (u'G', 3), 
 (u'A', 4), 
 (u'C', 2), 
 (u'T', 4), 
 (u'G', 2)
]
>>> baseCount = rdd.reduceByKey(lambda x,y : x+y)
>>> baseCount.collect()
[
 (u'A', 7), 
 (u'C', 6), 
 (u'G', 5), 
 (u'T', 7)
]
>>> 
````

	
