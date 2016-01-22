PySpark Tutorial
================
PySpark is the Spark Python API.  

Start PySpark
=============
First make sure that you have started the Spark cluster. To start Spark, you execute:

````
cd $SPRAK_HOME
./sbin/start-all.sh
````

To start PySpark, execute the following:

````
cd $SPRAK_HOME
./bin/pyspark
````

Successful execution will give you the PySpark prompt:

````
./bin/pyspark
Python 2.7.10 (default, Aug 22 2015, 20:33:39) 
[GCC 4.2.1 Compatible Apple LLVM 7.0.0 (clang-700.0.59.1)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
16/01/20 10:26:28 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /__ / .__/\_,_/_/ /_/\_\   version 1.6.0
      /_/

Using Python version 2.7.10 (default, Aug 22 2015 20:33:39)
SparkContext available as sc, HiveContext available as sqlContext.
>>> 
````

Note that the shell already have created a SparkContext (````sc````) object and you may use it to create RDDs.

Creating RDDs
=============
You may create RDDs by reading files from data structures, local file system, HDFS, and other data sources.

Create RDD from a Data Structure (or Collection)
------------------------------------------------
* Example-1

````
>>> data = [1, 2, 3, 4, 5, 8, 9]
>>> data
[1, 2, 3, 4, 5, 8, 9]
>>> myRDD = sc.parallelize(data)
>>> myRDD.collect()
[1, 2, 3, 4, 5, 8, 9]
>>> myRDD.count()
7
>>> 
````

* Example-2

````
>>> kv = [('a',7), ('a', 2), ('b', 2), ('b',4), ('c',1), ('c',2), ('c',3), ('c',4)]
>>> kv
[('a', 7), ('a', 2), ('b', 2), ('b', 4), ('c', 1), ('c', 2), ('c', 3), ('c', 4)]
>>> rdd2 = sc.parallelize(kv)
>>> rdd2.collect()
[('a', 7), ('a', 2), ('b', 2), ('b', 4), ('c', 1), ('c', 2), ('c', 3), ('c', 4)]
>>>
>>> rdd3 = rdd2.reduceByKey(lambda x, y : x+y)
>>> rdd3.collect()
[('a', 9), ('c', 10), ('b', 6)]
>>> 
````

* Example-3

````
# ./bin/pyspark 
Python 2.7.10 (default, Aug 22 2015, 20:33:39) 
[GCC 4.2.1 Compatible Apple LLVM 7.0.0 (clang-700.0.59.1)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
16/01/21 16:46:08 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /__ / .__/\_,_/_/ /_/\_\   version 1.6.0
      /_/

Using Python version 2.7.10 (default, Aug 22 2015 20:33:39)
SparkContext available as sc, HiveContext available as sqlContext.
>>> kv = [('a',7), ('a', 2), ('b', 2), ('b',4), ('c',1), ('c',2), ('c',3), ('c',4)]

>>> kv
[('a', 7), ('a', 2), ('b', 2), ('b', 4), ('c', 1), ('c', 2), ('c', 3), ('c', 4)]
>>> rdd2 = sc.parallelize(kv)
>>> rdd2.collect()
[('a', 7), ('a', 2), ('b', 2), ('b', 4), ('c', 1), ('c', 2), ('c', 3), ('c', 4)]

>>> rdd3 = rdd2.groupByKey()
>>> rdd3.collect()
[
 ('a', <pyspark.resultiterable.ResultIterable object at 0x104ec4c50>), 
 ('c', <pyspark.resultiterable.ResultIterable object at 0x104ec4cd0>), 
 ('b', <pyspark.resultiterable.ResultIterable object at 0x104ce7290>)
]

>>> rdd3.map(lambda x : (x[0], list(x[1]))).collect()
[
 ('a', [7, 2]), 
 ('c', [1, 2, 3, 4]), 
 ('b', [2, 4])
]
>>> 
````



Create RDD from a Local File System
-----------------------------------
````
import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.api.java.JavaSparkContext;
...
JavaSparkContext context = new JavaSparkContext();
...
final String inputPath ="file:///dir1/dir2/myinputfile.txt";
JavaRDD<String> rdd = context.textFile(inputPath);
...
````


Create RDD from HDFS
--------------------
* Example-1:

````
import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.api.java.JavaSparkContext;
...
JavaSparkContext context = new JavaSparkContext();
...
final String inputPath ="hdfs://myhadoopserver:9000/dir1/dir2/myinputfile.txt";
JavaRDD<String> rdd = context.textFile(inputPath);
...
````

* Example-2:

````
import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.api.java.JavaSparkContext;
...
JavaSparkContext context = new JavaSparkContext();
...
final String inputPath ="/dir1/dir2/myinputfile.txt";
JavaRDD<String> rdd = context.textFile(inputPath);
...
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
