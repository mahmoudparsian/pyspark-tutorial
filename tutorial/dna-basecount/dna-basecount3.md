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
unique bases. For this solution we use an external Python
function defined in ````basemapper.py````

* Define Python Function

````
$ export SPARK_HOME=/home/mparsian/spark-1.6.1-bin-hadoop2.6
$ cat $SPARK_HOME/basemapper.py
#!/usr/bin/python

def mapper(seq):
	freq = dict()
	for x in list(seq):
		if x in freq:
			freq[x] +=1
		else:
			freq[x] = 1
#
	kv = [(x, freq[x]) for x in freq]
	return kv
#
#for testing:
#print mapper("ATCGATCGATAT")	
````
* Define Very Basic Sample Input
 
````
$ cat /home/mparsian/dna_seq.txt
ATATCCCCGGGAT
ATCGATCGATAT
````

* Sample PySpark Run

````
# ./bin/pyspark
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /__ / .__/\_,_/_/ /_/\_\   version 1.6.1
      /_/

SparkContext available as sc, HiveContext available as sqlContext.
>>> recs = sc.texFile('file:///home/mparsian/dna_seq.txt')

>>> recs.collect()
[
 u'ATATCCCCGGGAT', 
 u'ATCGATCGATAT'
]

>>> basemapper = "/Users/mparsian/spark-1.6.1-bin-hadoop2.6/basemapper.py"
>>> import basemapper
>>> basemapper
<module 'basemapper' from 'basemapper.py'>
>>>
>>> recs = sc.textFile('file:////Users/mparsian/zmp/github/pyspark-tutorial/tutorial/dna-basecount/dna_seq.txt')
>>> rdd = recs.flatMap(basemapper.mapper)
>>> rdd.collect()
[(u'A', 3), (u'C', 4), (u'T', 3), (u'G', 3), (u'A', 4), (u'C', 2), (u'T', 4), (u'G', 2)]

>>> baseCount = rdd.reduceByKey(lambda x,y : x+y)
>>> baseCount.collect()
[(u'A', 7), (u'C', 6), (u'G', 5), (u'T', 7)]
>>>
````