PySpark Tutorial
================
The purpose of pyspark-tutorial is to provide basic algorithms using PySpark.
Note that PySpark is an interactive shell for basic testing and debugging and 
is not supposed to be used for production environment.

pyspark-tutorials
=================
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