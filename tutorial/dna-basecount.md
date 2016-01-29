DNA Base Counting using PySpark
===============================

DNA Base Count Definition
-------------------------
[DNA Base Counting is defined here.](https://www.safaribooksonline.com/library/view/data-algorithms/9781491906170/ch24.html)

Solution in PySpark
-------------------
This solution assumes that each record is a DNA sequence. 
This solution emits a ````(base, 1)```` for every base in 
a given sequence and then aggregates all frequencies for 
unique bases.


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

>>> ones = recs.flatMap(lambda x : [(c,1) for c in list(x)])
>>> ones.collect()
[
 (u'A', 1), 
 (u'T', 1), 
 (u'A', 1), 
 (u'T', 1), 
 (u'C', 1), 
 (u'C', 1), 
 (u'C', 1), 
 (u'C', 1), 
 (u'G', 1), 
 (u'G', 1), 
 (u'G', 1), 
 (u'A', 1), 
 (u'T', 1), 
 (u'A', 1), 
 (u'T', 1), 
 (u'C', 1), 
 (u'G', 1), 
 (u'A', 1), 
 (u'T', 1), 
 (u'C', 1), 
 (u'G', 1), 
 (u'A', 1), 
 (u'T', 1), 
 (u'A', 1), 
 (u'T', 1)
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

	
