# Download, Install, and Run PySpark

# 1. For macbook users: Enable "Remote Login"


      System Preferences --> Sharing --> enable "Remote Login" service



# 2. Make Sure Java 8 is Installed Properly

	java -version
	java version "1.8.0_72"
	Java(TM) SE Runtime Environment (build 1.8.0_72-b15)
	Java HotSpot(TM) 64-Bit Server VM (build 25.72-b15, mixed mode)


# 3. Download 

Download the latest binary Spark from the following URL:

	https://www.apache.org/dyn/closer.lua/spark/spark-3.3.0/spark-3.3.0-bin-hadoop3.tgz


# 4. Open the Downloaded File

Assuming that I have downloaded my file in 
`/home/mparsian/spark-3.3.0-bin-hadoop3.tgz`


	cd /home/mparsian

	tar zvfx  spark-3.3.0-bin-hadoop3.tgz
	x spark-3.3.0-bin-hadoop3/
	x spark-3.3.0-bin-hadoop3/NOTICE
	x spark-3.3.0-bin-hadoop3/CHANGES.txt
	...


# 5. Start the Spark Cluster

	cd /home/mparsian/spark-3.3.0-bin-hadoop3/

	./sbin/start-all.sh
	
	NOTE: If you are going to run Spark in your pc/macbook/windows, 
	then you do NOT need to start cluster at all. Invoking
	./bin/pyspark, your laptop is considered as your cluster 


# 6. Check Master and Worker

Make sure that Master and Worker processes are running:


	jps
	1347 Master
	1390 Worker


# 7. Check The Spark URL

	http://localhost:8080


# 8. Define Very Basic Python Program

* Python program: `/home/mparsian/spark-3.3.0-bin-hadoop3/test.py`

		#!/usr/bin/python
		import sys

		for line in sys.stdin:
			print "hello " + line
		

* Python program: `/home/mparsian/spark-3.3.0-bin-hadoop3/test2.py`	
	
		#!/usr/bin/python
		def fun2(str):
			str2 = str + " zaza"
			return str2


# 9. Start and Run pyspark

		cd /home/mparsian/spark-3.3.0-bin-hadoop3/
		./bin/pyspark
				...
		...
		Welcome to
			  ____              __
			 / __/__  ___ _____/ /__
			_\ \/ _ \/ _ `/ __/  '_/
		   /__ / .__/\_,_/_/ /_/\_\   version 3.3.0
			  /_/

		>>> data = ["john","paul","george","ringo"]
		>>> data
		['john', 'paul', 'george', 'ringo']

		>>> rdd = sc.parallelize(data)
		>>> rdd.collect()
		['john', 'paul', 'george', 'ringo']


		>>> test = "/home/mparsian/spark-3.3.0-bin-hadoop3/test.py"
		>>> test2 = "/home/mparsian/spark-3.3.0-bin-hadoop3/test2.py"
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

