How to Minimize the Verbosity of Spark
======================================
* Step-1: create a log4j.properties file
````
cp $SPARK_HOME/conf/log4j.properties.template $SPARK_HOME/conf/log4j.properties
````
* Step-2: Edit $SPARK_HOME/conf/log4j.properties file: replace "INFO" with "WARN"

* Now your file should look like:
````
cat $SPARK_HOME/conf/log4j.properties
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