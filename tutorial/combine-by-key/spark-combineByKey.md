Some Notes on Spark's combineByKey()
====================================

Spark's ````combineByKey()```` is invked like this:

````
rdd2 = rdd.combineByKey(createCombiner, mergeValue, mergeCombiners) 
````

To use Spark's combineByKey(), you need to define a 
data structure ````C```` (called combiner data structure)
and 3 basic functions:

* createCombiner
* mergeValue
* mergeCombiners

Generic function to combine the elements for each key using 
a custom set of aggregation functions.


Turns an ````RDD[(K, V)]```` into a result of type ````RDD[(K, C)]````, 
for a “combined type” ````C````. Note that ````V````and ````C```` can be 
different –  for example, one might group an RDD of type ````(Integer, Integer)```` 
into an RDD of type ````(Integer, List[Integer])````.

Users provide three lambda-based functions:

1. createCombiner, which turns a V into a C (e.g., creates a one-element list)
````
  V --> C
````

2. mergeValue, to merge a V into a C (e.g., adds it to the end of a list) 
````
  C, V --> C
````
  
3. mergeCombiners, to combine two C’s into a single one.
````
  C, C --> C
````

In addition, users can control the partitioning of the output RDD.

````
>>> data = [("a", 1), ("b", 1), ("a", 1)]
>>> x = sc.parallelize(data)
>>> def add(a, b): return a + str(b)
>>> sorted(x.combineByKey(str, add, add).collect())
[('a', '11'), ('b', '1')]
````

Example: Average By Key: use combineByKey()
===========================================

The example below uses data in the form of a list of key-value 
tuples: (key, value). First, we convert the list into a Spark's
Resilient Distributed Dataset (RDD) with ````sc.parallelize()````, 
where sc is an instance of pyspark.SparkContext.

The next step is to use combineByKey to compute the sum and count 
for each key in data. Here the combined data structure ````C```` 
is a pair of ````(sum, count)````. The 3 lambda-functions will be 
explained in detail in the following sections. The result, sumCount, 
is an RDD where its values are in the form of ````(key, (sum, count))````.

To compute the average-by-key, we use the ````map()```` method to divide 
the sum by the count for each key.

Finally, we may use the ````collectAsMap()```` method to return the average-by-key 
as a dictionary.

````
data = [
        (A, 2.), (A, 4.), (A, 9.), 
        (B, 10.), (B, 20.), 
        (Z, 3.), (Z, 5.), (Z, 8.), (Z, 12.) 
       ]

rdd = sc.parallelize( data )

sumCount = rdd.combineByKey(lambda value: (value, 1),
                            lambda x, value: (x[0] + value, x[1] + 1),
                            lambda x, y: (x[0] + y[0], x[1] + y[1])
                           )

averageByKey = sumCount.map(lambda (key, (totalSum, count)): (key, totalSum / count))

averageByKey.collectAsMap()

Result:

{
  A: 5.0, 
  B: 15.0
  Z: 7.0
}
````


The combineByKey Method
=======================
In order to aggregate an RDD's elements in parallel, Spark's combineByKey 
method requires three functions:

1. createCombiner
2. mergeValue
3. mergeCombiner

Create a Combiner
-----------------
````
lambda value: (value, 1)
````
The first required argument in the combineByKey method is a function to 
be used as the very first aggregation step for each key. The argument of 
this function corresponds to the value in a key-value pair. If we want to 
compute the sum and count using combineByKey, then we can create this 
"combiner" to be a tuple in the form of (sum, count). Note that (sum, count)
is the combine data structure ````C```` (in tha API). The very first 
step in this aggregation is then (value, 1), where value is the first 
RDD value that combineByKey comes across and 1 initializes the count.

Merge a Value
-------------
````
lambda x, value: (x[0] + value, x[1] + 1)
````
The next required function tells combineByKey what to do when a combiner 
is given a new value. The arguments to this function are a combiner and 
a new value. The structure of the combiner is defined above as a tuple 
in the form of (sum, count) so we merge the new value by adding it to the 
first element of the tuple while incrementing 1 to the second element of 
the tuple.

Merge two Combiners
-------------------
````
lambda x, y: (x[0] + y[0], x[1] + y[1])
````
The final required function tells combineByKey how to merge two combiners. 
In this example with tuples as combiners in the form of (sum, count), all 
we need to do is add the first and last elements together.

Compute the Average
-------------------
````
averageByKey = 
  sumCount.map(lambda (key, (totalSum, count)): (key, totalSum / count))
````

Ultimately the goal is to compute the average-by-key. The result from 
combineByKey is an RDD with elements in the form (label, (totalSum, count)), 
so the average-by-key can easily be obtained by using the map method, 
mapping (totalSum, count) to totalSum / count.
We should not use ````sum```` as variable name in the PySpark code because it is a 
built-in function in Python.


Let's break up the data into 2 partitions (just as an example) 
and see it in action:

````
data = [
        ("A", 2.), ("A", 4.), ("A", 9.), 
        ("B", 10.), ("B", 20.), 
        ("Z", 3.), ("Z", 5.), ("Z", 8.), ("Z", 12.) 
       ]

Partition 1: ("A", 2.), ("A", 4.), ("A", 9.), ("B", 10.)
Partition 2: ("B", 20.), ("Z", 3.), ("Z", 5.), ("Z", 8.), ("Z", 12.) 


Partition 1 
("A", 2.), ("A", 4.), ("A", 9.), ("B", 10.)

A=2. --> createCombiner(2.) ==> accumulator[A] = (2., 1)
A=4. --> mergeValue(accumulator[A], 4.) ==> accumulator[A] = (2. + 4., 1 + 1) = (6., 2)
A=9. --> mergeValue(accumulator[A], 9.) ==> accumulator[A] = (6. + 9., 2 + 1) = (15., 3)
B=10. --> createCombiner(10.) ==> accumulator[B] = (10., 1)

Partition 2
("B", 20.), ("Z", 3.), ("Z", 5.), ("Z", 8.), ("Z", 12.) 

B=20. --> createCombiner(20.) ==> accumulator[B] = (20., 1)
Z=3. --> createCombiner(3.) ==> accumulator[Z] = (3., 1)
Z=5. --> mergeValue(accumulator[Z], 5.) ==> accumulator[Z] = (3. + 5., 1 + 1) = (8., 2)
Z=8. --> mergeValue(accumulator[Z], 8.) ==> accumulator[Z] = (8. + 8., 2 + 1) = (16., 3)
Z=12. --> mergeValue(accumulator[Z], 12.) ==> accumulator[Z] = (16. + 12., 3 + 1) = (28., 4)

Merge partitions together
A ==> (15., 3)
B ==> mergeCombiner((10., 1), (20., 1)) ==> (10. + 20., 1 + 1) = (30., 2)
Z ==> (28., 4)

So, you should get back an array something like this:

Array( [A, (15., 3)], [B, (30., 2)], [Z, (28., 4)])

````
