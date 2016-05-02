Spark's mapPartitions()
=======================

According to Spark API: ````mapPartitions(func)````	transformation is 
similar to ````map()````, but runs separately on each partition (block) 
of the RDD, so ````func```` must be of type ````Iterator<T> => Iterator<U>````
when running on an RDD of type T.


The ````mapPartitions()```` transformation should be used when you want to 
extract some condensed information (such as finding the minimum and maximum 
of numbers) from each partition. For example, if you want to find the minimum 
and maximum of all numbers in your input, then using ````map()```` can be 
pretty inefficient, since you will be generating tons of intermediate 
(K,V) pairs, but the bottom line is you just want to find two numbers: the 
minimum and maximum of all numbers in your input. Another example can be if 
you want to find top-10 (or bottom-10) for your input, then mapPartitions() 
can work very well: find the top-10 (or bottom-10) per partition, then find 
the top-10 (or bottom-10) for all partitions: this way you are limiting 
emitting too many intermediate (K,V) pairs.


Example-1: Sum Each Partition
=============================
````
>>> numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> numbers
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

>>> rdd = sc.parallelize(numbers, 3)

>>> rdd.collect()
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

>>> rdd.getNumPartitions()
3

>>> def f(iterator):
...     for x in iterator:
...             print(x)
...     print "==="
...
>>> rdd.foreachPartition(f)
1
2
3
===
7
8
9
10
===
4
5
6
===

>>> def adder(iterator):
...     yield sum(iterator)
...
>>> rdd.mapPartitions(adder).collect()
[6, 15, 34]

````


Example-2: Find Minimum and Maximum
===================================
Use ````mapPartitions()```` and find the minimum and maximum from each partition.

To make it a cleaner solution, we define a python function to return the minimum and maximum 
for a given iteration.

````
$ cat minmax.py
#!/usr/bin/python

def minmax(iterator):
	firsttime = 0
	#min = 0;
	#max = 0;
	for x in iterator:
		if (firsttime == 0):
			min = x;
			max = x;
			firsttime = 1
		else:
			if x > max:
				max = x
			if x < min:
				min = x
		#
	return (min, max)
#
#data = [10, 20, 3, 4, 5, 2, 2, 20, 20, 10]
#print minmax(data)	
````
Then we use the minmax function for the ````mapPartitions()````:

````
### NOTE: data  can be huge, but for understanding 
### the mapPartitions() we use a very small data set

>>> data = [10, 20, 3, 4, 5, 2, 2, 20, 20, 10]
>>> rdd = sc.parallelize(data, 3)

>>> rdd.getNumPartitions()
3

>>> rdd.collect()
[10, 20, 3, 4, 5, 2, 2, 20, 20, 10]

>>> def f(iterator):
...     for x in iterator:
...             print(x)
...     print "==="
... ^D

>>> rdd.foreachPartition(f)
10
20
3
===
4
5
2
===
2
20
20
10
===
>>>

>>> minmax = "/Users/mparsian/spark-1.6.1-bin-hadoop2.6/minmax.py"
>>> import minmax

### NOTE: the minmaxlist is a small list of numbers 
### two mumbers (min and max) are generated per partition
>>> minmaxlist = rdd.mapPartitions(minmax.minmax).collect()
>>> minmaxlist 
[3, 20, 2, 5, 2, 20]

>>> min(minmaxlist)
2
>>> max(minmaxlist)
20
````

Questions/Comments
==================
* [View Mahmoud Parsian's profile on LinkedIn](http://www.linkedin.com/in/mahmoudparsian)
* Please send me an email: mahmoud.parsian@yahoo.com
* [Twitter: @mahmoudparsian](http://twitter.com/mahmoudparsian)

Thank you!

````
best regards,
Mahmoud Parsian
````

[![Data Algorithms Book](https://github.com/mahmoudparsian/data-algorithms-book/blob/master/misc/data_algorithms_image.jpg)](http://shop.oreilly.com/product/0636920033950.do)
