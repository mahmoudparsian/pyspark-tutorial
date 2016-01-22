PySpark Tutorial
================
PySpark is the Spark Python API.  The purpose of PySpark tutorial is to provide basic distributed algorithms using PySpark. Note that PySpark is an interactive shell for basic testing and debugging and is not supposed to be used for production environment.

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
[('a', <pyspark.resultiterable.ResultIterable object at 0x104ec4c50>), ('c', <pyspark.resultiterable.ResultIterable object at 0x104ec4cd0>), ('b', <pyspark.resultiterable.ResultIterable object at 0x104ce7290>)]

>>> rdd3.map(lambda x : (x[0], list(x[1]))).collect()
[('a', [7, 2]), ('c', [1, 2, 3, 4]), ('b', [2, 4])]
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



PySpark Examples and Tutorials
==============================
* wordcount: classic word count
* bigrams: find frequency of bigrams
* basic-join: basic join of two relations R(K, V1), S(K,V2)
* basic-map: basic mapping of RDD elements
* basic-add: how to add all RDD elements together
* basic-multiply: how to multiply all RDD elements together
* top-N: find top-N and bottom-N
* combine-by-key: find average by using combineByKey()
* basic-filter: how to filter RDD elements
* basic-average: how to find average
* cartesian: rdd1.cartesian(rdd2)
* basic-sort: sortByKey ascending/descending

How to Minimize the Verbosity of Spark
======================================
* Step-1: create a log4j.properties file
````
cp $SPARK_HOME/conf/log4j.properties.template $SPARK_HOME/conf/log4j.properties
````
* Step-2: Edit $SPARK_HOME/conf/log4j.properties file: replace "INFO" with "WARN"

* Now your file should look like:
````
cat spark-1.3.0/conf/log4j.properties
# Set everything to be logged to the console
log4j.rootCategory=WARN, console
log4j.appender.console=org.apache.log4j.ConsoleAppender
log4j.appender.console.target=System.err
log4j.appender.console.layout=org.apache.log4j.PatternLayout
log4j.appender.console.layout.ConversionPattern=%d{yy/MM/dd HH:mm:ss} %p %c{1}: %m%n

# Settings to quiet third party logs that are too verbose
log4j.logger.org.eclipse.jetty=WARN
log4j.logger.org.eclipse.jetty.util.component.AbstractLifeCycle=ERROR
log4j.logger.org.apache.spark.repl.SparkIMain$exprTyper=WARN
log4j.logger.org.apache.spark.repl.SparkILoop$SparkILoopInterpreter=WARN
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
