Download, Install, and Run PySpark
==================================

0. For macbook users: Enable "Remote Login"
==========================================
````
System Preferences --> Sharing --> enable "Remote Login" service
````

1. Make Sure Java is Installed Properly
=======================================
````
java -version
java version "1.8.0_72"
Java(TM) SE Runtime Environment (build 1.8.0_72-b15)
Java HotSpot(TM) 64-Bit Server VM (build 25.72-b15, mixed mode)
````

2. Download 
===========
Download the latest binary Spark from the following URL:
````
http://www.apache.org/dyn/closer.lua/spark/spark-1.6.1/spark-1.6.1-bin-hadoop2.6.tgz
````

3. Open the Downloaded File
===========================
Assuming that I have downloaded my file in /Users/mparsian/spark-1.6.1-bin-hadoop2.6.tgz

````
cd /Users/mparsian

tar zvfx  spark-1.6.1-bin-hadoop2.6.tgz
x spark-1.6.1-bin-hadoop2.6/
x spark-1.6.1-bin-hadoop2.6/NOTICE
x spark-1.6.1-bin-hadoop2.6/CHANGES.txt
...
...
...
x spark-1.6.1-bin-hadoop2.6/lib/spark-examples-1.6.1-hadoop2.6.0.jar
x spark-1.6.1-bin-hadoop2.6/README.md
````

4. Start the Spark Cluster
==========================
````
cd /Users/mparsian/spark-1.6.1-bin-hadoop2.6/

ls -l
total 2736
-rw-r--r--@  1 mparsian  897801646  1343562 Feb 26 21:02 CHANGES.txt
-rw-r--r--@  1 mparsian  897801646    17352 Feb 26 21:02 LICENSE
-rw-r--r--@  1 mparsian  897801646    23529 Feb 26 21:02 NOTICE
drwxr-xr-x@  3 mparsian  897801646      102 Feb 26 21:02 R
-rw-r--r--@  1 mparsian  897801646     3359 Feb 26 21:02 README.md
-rw-r--r--@  1 mparsian  897801646      120 Feb 26 21:02 RELEASE
drwxr-xr-x@ 25 mparsian  897801646      850 Feb 26 21:02 bin
drwxr-xr-x@  9 mparsian  897801646      306 Feb 26 21:02 conf
drwxr-xr-x@  3 mparsian  897801646      102 Feb 26 21:02 data
drwxr-xr-x@  6 mparsian  897801646      204 Feb 26 21:02 ec2
drwxr-xr-x@  3 mparsian  897801646      102 Feb 26 21:02 examples
drwxr-xr-x@  8 mparsian  897801646      272 Feb 26 21:02 lib
drwxr-xr-x@ 37 mparsian  897801646     1258 Feb 26 21:02 licenses
drwxr-xr-x@  9 mparsian  897801646      306 Feb 26 21:02 python
drwxr-xr-x@ 24 mparsian  897801646      816 Feb 26 21:02 sbin


./sbin/start-all.sh
````

5. Check Master and Worker
==========================
Make sure that Master and Worker processes are running:

````
jps
1347 Master
1390 Worker
````

6. Check The Spark URL
======================

````
http://localhost:8080
````

7. Define 2 Very Basic Python Programs
======================================

* Python program: ````test.py````

````
cat /Users/mparsian/spark-1.6.1-bin-hadoop2.6/test.py
#!/usr/bin/python

import sys

for line in sys.stdin:
	print "hello " + line
````

* Python program: ````test2.py````
	
````	
cat /Users/mparsian/spark-1.6.1-bin-hadoop2.6/test2.py
#!/usr/bin/python

def fun2(str):
	str2 = str + " zaza"
	return str2
````

8. Start and Run pyspark
========================
````
cd /Users/mparsian/spark-1.6.1-bin-hadoop2.6/
./bin/pyspark
Python 2.7.10 (default, Oct 23 2015, 19:19:21)
[GCC 4.2.1 Compatible Apple LLVM 7.0.0 (clang-700.0.59.5)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
16/04/04 11:18:01 INFO spark.SparkContext: Running Spark version 1.6.1
...
...
...
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /__ / .__/\_,_/_/ /_/\_\   version 1.6.1
      /_/

Using Python version 2.7.10 (default, Oct 23 2015 19:19:21)
SparkContext available as sc, HiveContext available as sqlContext.

>>> data = ["john","paul","george","ringo"]
>>> data
['john', 'paul', 'george', 'ringo']

>>> rdd = sc.parallelize(data)
>>> rdd.collect()
['john', 'paul', 'george', 'ringo']


>>> test = "/Users/mparsian/spark-1.6.1-bin-hadoop2.6/test.py"
>>> test2 = "/Users/mparsian/spark-1.6.1-bin-hadoop2.6/test2.py"
>>> import test
>>> import test2


>>> pipeRDD =  rdd.pipe(test)
>>> pipeRDD.collect()
[u'hello john', u'', u'hello paul', u'', u'hello george', u'', u'hello ringo', u'']


>>> rdd.collect()
['john', 'paul', 'george', 'ringo']


>>> rdd2 = rdd.map(lambda x : test2.fun2(x))
>>> rdd2.collect()
['john zaza', 'paul zaza', 'george zaza', 'ringo zaza']
>>>
````
