# define Spark's installed directory
export SPARK_HOME="/Users/mparsian/spark-2.2.1"
#
# define your input path
INPUT_PATH="file:///Users/mparsian/spark-2.2.1/zbin/sample.txt"
#
# define your PySpark program
PROG="/Users/mparsian/zmp/github/pyspark-tutorial/tutorial/wordcount/word_count_ver2.py"
#
# submit your spark application
$SPARK_HOME/bin/spark-submit $PROG $INPUT_PATH
