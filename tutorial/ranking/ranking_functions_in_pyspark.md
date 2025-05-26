# Ranking Functions in PySpark
### Using Ranking Functions in PySpark DataFrames


Last updated: May 25, 2025

* Ranking functions are important in SQL: 
  used in OLAP queries for data warehousing. 

* We can apply ranking functions for RDDs in PySpark.

* Ranking functions are typically used with **DataFrames** 
  rather than **RDDs**. 

* PySpark provides built-in ranking functions 
  such as `rank()`, `dense_rank()`, and `row_number()` 
  that work within **window specifications**.

* Here are complete and detailed examples of ranking 
  functions in PySpark with IO and its equivalent in SQL.

## Example 1

Here’s an example of how you can apply ranking functions in PySpark:

```python
from pyspark.sql import SparkSession
from pyspark.sql.window import Window
from pyspark.sql.functions import rank
from pyspark.sql.functions import dense_rank
from pyspark.sql.functions import row_number

# Initialize Spark session
spark = SparkSession.builder.getOrCreate()

# Sample DataFrame
data = [(1, "Alice", 100),
        (2, "Bob", 200),
        (3, "Charlie", 200),
        (4, "David", 150)]

columns = ["id", "name", "score"]
df = spark.createDataFrame(data, columns)

# Define window specification
window_spec = Window.orderBy(df["score"].desc())

# Apply ranking functions
df = df.withColumn("rank", rank().over(window_spec))
df = df.withColumn("dense_rank", dense_rank().over(window_spec))
df = df.withColumn("row_number", row_number().over(window_spec))

# Show results
df.show()
```

### 🚀 Why Not Use RDDs?

RDDs are **low-level** and do not support built-in 
ranking functions like DataFrames do. If you must 
use RDDs, you would need to manually implement ranking 
logic using transformations like `map()` and `sortBy()`, 
which is **less efficient** compared to using DataFrames.

Here are examples of other ranking functions in PySpark.
PySpark provides several ranking functions that can be 
used within **window specifications** to rank rows based 
on specific criteria. Here are some additional ranking 
functions:

### 1. **`percent_rank()`**
   - Returns the **relative rank** of rows within a partition as a percentage.
   - Formula: `(rank - 1) / (total_rows - 1)`

### 2. **`dense_rank()`**
   - Similar to `rank()`, but **without gaps** in ranking when there are ties.

### 3. **`ntile(n)`**
   - Divides rows into **n equal groups** and assigns a bucket number to each row.

### 4. **`cume_dist()`**
   - Computes the **cumulative distribution** of values within a partition.


## Example 2

```python
from pyspark.sql import SparkSession
from pyspark.sql.window import Window
from pyspark.sql.functions import percent_rank
from pyspark.sql.functions import dense_rank
from pyspark.sql.functions import ntile
from pyspark.sql.functions import cume_dist

# Initialize Spark session
spark = SparkSession.builder.getOrCreate()

# Sample DataFrame
data = [(1, "Alice", 100),
        (2, "Bob", 200),
        (3, "Charlie", 200),
        (4, "David", 150)]

columns = ["id", "name", "score"]
df = spark.createDataFrame(data, columns)

# Define window specification
window_spec = Window.orderBy(df["score"].desc())

# Apply ranking functions
df = df.withColumn("percent_rank", percent_rank().over(window_spec))
df = df.withColumn("dense_rank", dense_rank().over(window_spec))
df = df.withColumn("ntile", ntile(3).over(window_spec))
df = df.withColumn("cume_dist", cume_dist().over(window_spec))

# Show results
df.show()
```

You can find more details on PySpark ranking functions 
[here](https://sparkbyexamples.com/pyspark/pyspark-window-functions/) 
and [here](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.functions.rank.html). 



## Example 3: `rank()` Function

Ranks rows within a partition, leaving gaps when 
there are ties.

#### **PySpark Example**
```python
from pyspark.sql import SparkSession
from pyspark.sql.window import Window
from pyspark.sql.functions import rank

spark = SparkSession.builder..getOrCreate()

data = [(1, "Alice", 100), 
        (2, "Bob", 200), 
        (3, "Charlie", 200), 
        (4, "David", 150)]
columns = ["id", "name", "score"]
df = spark.createDataFrame(data, columns)

window_spec = Window.orderBy(df["score"].desc())
df = df.withColumn("rank", rank().over(window_spec))

df.show()
```

#### **SQL Equivalent**
```sql
SELECT 
       id, 
       name, 
       score, 
       RANK() OVER (ORDER BY score DESC) AS rnk
FROM 
     my_table;
```

#### **Output**
```
+---+-------+-----+----+
|id |name   |score|rnk |
+---+-------+-----+----+
|2  |Bob    |200  |1   |
|3  |Charlie|200  |1   |
|4  |David  |150  |3   |
|1  |Alice  |100  |4   |
+---+-------+-----+----+
```

---

## Example 4:  `dense_rank()` Function

Similar to `rank()`, but **without gaps** in ranking.

#### **PySpark Example**
```python
from pyspark.sql.functions import dense_rank

df = df.withColumn("dense_rank", dense_rank().over(window_spec))
df.show()
```

#### **SQL Equivalent**
```sql
SELECT 
      id, 
      name, 
      score, 
      DENSE_RANK() OVER (ORDER BY score DESC) AS dense_rnk
FROM 
      my_table;
```

#### **Output**
```
+---+-------+-----+----------+
|id |name   |score| dense_rnk|
+---+-------+-----+----------+
|2  |Bob    |200  |1         |
|3  |Charlie|200  |1         |
|4  |David  |150  |2         |
|1  |Alice  |100  |3         |
+---+-------+-----+----------+
```

---

## Example 5: `row_number()` Function

Assigns a **unique sequential number** to each row.

#### **PySpark Example**
```python
from pyspark.sql.functions import row_number

df = df.withColumn("row_number", row_number().over(window_spec))
df.show()
```

#### **SQL Equivalent**
```sql
SELECT 
      id, 
      name, 
      score, 
      ROW_NUMBER() OVER (ORDER BY score DESC) AS row_num
FROM 
      my_table;
```

#### **Output**
```
+---+-------+-----+--------+
|id |name   |score|row_num |
+---+-------+-----+--------+
|2  |Bob    |200  |1       |
|3  |Charlie|200  |2       |
|4  |David  |150  |3       |
|1  |Alice  |100  |4       |
+---+-------+-----+--------+
```

---

## Example 6: `percent_rank()` Function

Calculates the **relative rank** of rows as a percentage.

#### **PySpark Example**
```python
from pyspark.sql.functions import percent_rank

df = df.withColumn("percent_rank", percent_rank().over(window_spec))
df.show()
```

#### **SQL Equivalent**
```sql
SELECT 
      id, 
      name, 
      score, 
      PERCENT_RANK() OVER (ORDER BY score DESC) AS perct_rank
FROM 
      my_table;
```

#### **Output**
```
+---+-------+-----+-----------+
|id |name   |score|perct_rank |
+---+-------+-----+-----------+
|2  |Bob    |200  |0.0        |
|3  |Charlie|200  |0.0        |
|4  |David  |150  |0.5        |
|1  |Alice  |100  |0.75       |
+---+-------+-----+-----------+
```

---

## Example 7: `ntile(n)` Function

Divides rows into **n equal groups**.

#### **PySpark Example**
```python
from pyspark.sql.functions import ntile

df = df.withColumn("ntile", ntile(3).over(window_spec))
df.show()
```

#### **SQL Equivalent**
```sql
SELECT 
      id, 
      name, 
      score, NTILE(3) OVER (ORDER BY score DESC) AS n_tile
FROM 
      my_table;
```

#### **Output**
```
+---+-------+-----+------+
|id |name   |score|n_tile|
+---+-------+-----+------+
|2  |Bob    |200  |1     |
|3  |Charlie|200  |1     |
|4  |David  |150  |2     |
|1  |Alice  |100  |3     |
+---+-------+-----+------+
```

---

## Example 8: `cume_dist()` Function

Computes the **cumulative distribution** of values.

#### **PySpark Example**
```python
from pyspark.sql.functions import cume_dist

df = df.withColumn("cume_dist", cume_dist().over(window_spec))
df.show()
```

#### **SQL Equivalent**
```sql
SELECT 
      id, 
      name, 
      score, 
      CUME_DIST() OVER (ORDER BY score DESC) AS c_dist
FROM 
     my_table;
```

#### **Output**
```
+---+-------+-----+--------+
|id |name   |score|c_dist  |
+---+-------+-----+--------+
|2  |Bob    |200  |0.5     |
|3  |Charlie|200  |0.5     |
|4  |David  |150  |0.75    |
|1  |Alice  |100  |1.0     |
+---+-------+-----+--------+
```

---

### **Summary of Ranking Functions**
| Function       | Description |
|---------------|-------------|
| `rank()`      | Assigns rank with gaps for ties |
| `dense_rank()`| Assigns rank without gaps |
| `row_number()`| Assigns unique sequential numbers |
| `percent_rank()` | Computes relative rank as a percentage |
| `ntile(n)`    | Divides rows into `n` equal groups |
| `cume_dist()` | Computes cumulative distribution |


You can find more details on PySpark ranking functions 
[here](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.functions.rank.html) 
and [here](https://sparkbyexamples.com/pyspark/pyspark-window-functions/). 

## Example 9: Row Number

**Input DataFrame:**

```
+---+-----+----------+------+
|id |name |department|salary|
+---+-----+----------+------+
|1  |John |Sales     |5000  |
|2  |Jane |Sales     |6000  |
|3  |Bob  |IT        |7000  |
|4  |Alice|IT        |5500  |
+---+-----+----------+------+
```

**PySpark:**

```python
from pyspark.sql.window import Window
from pyspark.sql.functions import row_number

window_spec = Window.partitionBy("department").orderBy("salary")
df = df.withColumn("row_num", row_number().over(window_spec))
df.show()
```

**SQL:**

```sql
SELECT
    *,
    ROW_NUMBER() OVER(PARTITION BY department ORDER BY salary) AS row_num
FROM employees;
```

**Output:**

```
+---+-----+----------+------+-------+
|id |name |department|salary|row_num|
+---+-----+----------+------+-------+
|4  |Alice|IT        |5500  |1      |
|3  |Bob  |IT        |7000  |2      |
|1  |John |Sales     |5000  |1      |
|2  |Jane |Sales     |6000  |2      |
+---+-----+----------+------+-------+
```

## Example 10:  Rank (with ties)

**Input DataFrame:**

```
+---+-----+----------+------+
|id |name |department|salary|
+---+-----+----------+------+
|1  |John |Sales     |5000  |
|2  |Jane |Sales     |6000  |
|3  |Bob  |IT        |5500  |
|4  |Alice|IT        |5500  |
+---+-----+----------+------+
```

**PySpark:**

```python
from pyspark.sql.functions import rank

df = df.withColumn("rank", rank().over(window_spec))
df.show()
```

**SQL:**

```sql
SELECT
    *,
    RANK() OVER(PARTITION BY department ORDER BY salary) AS rank
FROM employees;
```

**Output:**

```
+---+-----+----------+------+----+
|id |name |department|salary|rank|
+---+-----+----------+------+----+
|3  |Bob  |IT        |5500  |1   |
|4  |Alice|IT        |5500  |1   |
|1  |John |Sales     |5000  |1   |
|2  |Jane |Sales     |6000  |2   |
+---+-----+----------+------+----+
```

## Example 11:  Dense Rank

**PySpark:**

```python
from pyspark.sql.functions import dense_rank

df = df.withColumn("dense_rank", dense_rank().over(window_spec))
df.show()
```

**SQL:**

```sql
SELECT
    *,
    DENSE_RANK() OVER(PARTITION BY department ORDER BY salary) AS dense_rank
FROM employees;
```

**Output:**

```
+---+-----+----------+------+----------+
|id |name |department|salary|dense_rank|
+---+-----+----------+------+----------+
|3  |Bob  |IT        |5500  |1         |
|4  |Alice|IT        |5500  |1         |
|1  |John |Sales     |5000  |1         |
|2  |Jane |Sales     |6000  |2         |
+---+-----+----------+------+----------+
```

## Example 12:  Percent Rank

**Input DataFrame:**

```
+---+-----+----------+------+
|id |name |department|salary|
+---+-----+----------+------+
|1  |John |Sales     |4000  |
|2  |Jane |Sales     |5000  |
|3  |Bob  |Sales     |6000  |
|4  |Alice|IT        |7000  |
+---+-----+----------+------+
```

**PySpark:**

```python
from pyspark.sql.functions import percent_rank

df = df.withColumn("percent_rank", percent_rank().over(window_spec))
df.show()
```

**SQL:**

```sql
SELECT
    *,
    PERCENT_RANK() OVER(PARTITION BY department ORDER BY salary) AS percent_rank
FROM employees;
```

**Output:**

```
+---+-----+----------+------+------------+
|id |name |department|salary|percent_rank|
+---+-----+----------+------+------------+
|4  |Alice|IT        |7000  |0.0         |
|1  |John |Sales     |4000  |0.0         |
|2  |Jane |Sales     |5000  |0.5         |
|3  |Bob  |Sales     |6000  |1.0         |
+---+-----+----------+------+------------+
```

## Example 13: NTILE (Dividing into 2 groups)

**PySpark:**

```python
from pyspark.sql.functions import ntile

df = df.withColumn("ntile", ntile(2).over(window_spec))
df.show()
```

**SQL:**

```sql
SELECT
    *,
    NTILE(2) OVER(PARTITION BY department ORDER BY salary) AS ntile
FROM employees;
```

**Output:**

```
+---+-----+----------+------+-----+
|id |name |department|salary|ntile|
+---+-----+----------+------+-----+
|4  |Alice|IT        |7000  |1    |
|1  |John |Sales     |4000  |1    |
|2  |Jane |Sales     |5000  |1    |
|3  |Bob  |Sales     |6000  |2    |
+---+-----+----------+------+-----+
```


## Example 14: Cumulative Distribution

**PySpark:**

```python
from pyspark.sql.functions import cume_dist

df = df.withColumn("cume_dist", cume_dist().over(window_spec))
df.show()
```

**SQL:**

```sql
SELECT
    *,
    CUME_DIST() OVER(PARTITION BY department ORDER BY salary) AS cume_dist
FROM employees;
```

**Output:**

```
+---+-----+----------+------+---------+
|id |name |department|salary|cume_dist|
+---+-----+----------+------+---------+
|4  |Alice|IT        |7000  |1.0      |
|1  |John |Sales     |4000  |0.333... |
|2  |Jane |Sales     |5000  |0.666... |
|3  |Bob  |Sales     |6000  |1.0      |
+---+-----+----------+------+---------+
```

## Example 15: Ranking with Multiple Ordering Criteria

**Input DataFrame:**

```
+---+-----+----------+------+----------+
|id |name |department|salary|hire_date |
+---+-----+----------+------+----------+
|1  |John |Sales     |5000  |2020-01-15|
|2  |Jane |Sales     |5000  |2019-03-10|
|3  |Bob  |IT        |7000  |2021-02-20|
|4  |Alice|IT        |5500  |2020-11-05|
+---+-----+----------+------+----------+
```

**PySpark:**

```python
from pyspark.sql.functions import col

complex_window = Window.partitionBy("department")
                       .orderBy(col("salary")
                       .desc(), 
                       col("hire_date").asc())
df = df.withColumn("complex_rank", row_number().over(complex_window))
df.show()
```

**SQL:**

```sql
SELECT
    *,
    ROW_NUMBER() OVER(
        PARTITION BY department
        ORDER BY salary DESC, hire_date ASC
    ) AS complex_rank
FROM employees;
```

**Output:**

```
+---+-----+----------+------+----------+------------+
|id |name |department|salary|hire_date |complex_rank|
+---+-----+----------+------+----------+------------+
|3  |Bob  |IT        |7000  |2021-02-20|1           |
|4  |Alice|IT        |5500  |2020-11-05|2           |
|2  |Jane |Sales     |5000  |2019-03-10|1           |
|1  |John |Sales     |5000  |2020-01-15|2           |
+---+-----+----------+------+----------+------------+
```

## Example 16: Ranking with Dynamic Partition Size

**PySpark:**

```python
from pyspark.sql.functions import count, lit

window_with_size = Window.partitionBy("department")
df = (df.withColumn("dept_size", count(lit(1)).over(window_with_size))
        .withColumn("size_adjusted_rank",
                   (rank().over(window_spec) / col("dept_size"))))
df.show()
```

**SQL:**

```sql
WITH dept_sizes AS (
    SELECT
        department,
        COUNT(*) AS dept_size
    FROM employees
    GROUP BY department
)
SELECT
    e.*,
    RANK() OVER(PARTITION BY e.department ORDER BY e.salary) / ds.dept_size AS size_adjusted_rank
FROM employees e
JOIN dept_sizes ds ON e.department = ds.department;
```

**Output:**

```
+---+-----+----------+------+---------+------------------+
|id |name |department|salary|dept_size|size_adjusted_rank|
+---+-----+----------+------+---------+------------------+
|4  |Alice|IT        |5500  |2        |0.5               |
|3  |Bob  |IT        |7000  |2        |1.0               |
|1  |John |Sales     |5000  |2        |0.5               |
|2  |Jane |Sales     |6000  |2        |1.0               |
+---+-----+----------+------+---------+------------------+
```

## Example 17: Conditional Ranking (Active employees only)

**Input DataFrame:**

```
+---+-----+----------+------+--------+
|id |name |department|salary|is_active|
+---+-----+----------+------+--------+
|1  |John |Sales     |5000  |true    |
|2  |Jane |Sales     |6000  |false   |
|3  |Bob  |IT        |7000  |true    |
|4  |Alice|IT        |5500  |true    |
+---+-----+----------+------+--------+
```

**PySpark:**

```python
from pyspark.sql.functions import when

df = df.withColumn("conditional_rank",
                  when(col("is_active") == True, rank().over(window_spec))
                  .otherwise(None))
df.show()
```

**SQL:**

```sql
SELECT
    *,
    CASE
        WHEN is_active = TRUE THEN
            RANK() OVER(PARTITION BY department ORDER BY salary)
        ELSE NULL
    END AS conditional_rank
FROM employees;
```

**Output:**

```
+---+-----+----------+------+--------+---------------+
|id |name |department|salary|is_active|conditional_rank|
+---+-----+----------+------+--------+---------------+
|4  |Alice|IT        |5500  |true    |1              |
|3  |Bob  |IT        |7000  |true    |2              |
|1  |John |Sales     |5000  |true    |1              |
|2  |Jane |Sales     |6000  |false   |null           |
+---+-----+----------+------+--------+---------------+
```

