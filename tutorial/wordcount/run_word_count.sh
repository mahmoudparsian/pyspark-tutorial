# define Spark's installed directory
export SPARK_HOME="/Users/mparsian/spark-2.2.1"
#
# define your input path
#INPUT_PATH="$SPARK_HOME/licenses/LICENSE-heapq.txt"
#
# define your PySpark program
PROG="/Users/mparsian/zmp/pyspark_book_project/programs/word_count.py"
#
# submit your spark application
$SPARK_HOME/bin/spark-submit $PROG 
