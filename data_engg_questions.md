Data Engineering Fundamentals

✅ 15 Core Questions

Explain the difference between ETL and ELT. When would you prefer one over the other?

What is Data Lake vs Data Warehouse vs Data Mart?

How do you handle schema evolution in a data pipeline?

What is partitioning and bucketing? How do they impact performance?

Explain the concept of data lineage and why it’s important.

What are the different types of slowly changing dimensions (SCD)? Which one is hardest to implement?

What’s the difference between batch processing and streaming? Give examples.

How do you design a pipeline to handle late-arriving data?

What are common data quality checks in production data pipelines?

Explain CAP theorem and its significance in distributed data systems.

What is shuffling in distributed systems? Why is it expensive?

Difference between horizontal and vertical scaling in data systems.

How do you handle idempotency in data pipelines?

Explain CDC (Change Data Capture). When is it useful?

What are the pros and cons of using Parquet vs ORC vs Avro file formats?

🔥 10 Complex Questions

You have 2 billion records updating daily in a fact table. How would you design the ingestion pipeline for high efficiency?

Your pipeline is failing intermittently due to schema drift. Walk me through how you would debug & fix it.

You have a data lake with petabytes of data — how do you design a data governance framework?

How would you minimize small file problems in Hadoop/S3?

Explain how you’d build a data pipeline that ensures exactly-once processing in a streaming use case.

How do you design a multi-region highly available data platform?

If a job runs 100x slower in production than in dev, what’s your debugging approach?

How would you implement audit logging for all transformations in a pipeline?

A source system delivers data with 5 min lag, but business requires near real-time dashboards. How do you bridge the gap?

You are asked to migrate a legacy ETL (Informatica) workflow to modern Spark-based architecture. How would you approach it?



🔹 2. PySpark

✅ 15 Core Questions
Difference between DataFrame, Dataset, and RDD.

What are narrow vs wide transformations in Spark? Give examples.

Explain lazy evaluation in Spark. Why is it important?

How does Spark handle shuffles?

Difference between map() and flatMap().

How does Spark manage DAG execution?

Explain caching vs persistence in Spark.

What is the difference between groupBy() and reduceByKey()?

How do broadcast variables help in Spark?

Explain checkpointing and when to use it.

How does Spark handle skewed data?

Explain coalesce() vs repartition().

How do you tune Spark executors and partitions for performance?

What is the difference between Structured Streaming and Spark Streaming?

Explain Tungsten and Catalyst optimizers.

🔥 10 Complex Questions
You have a Spark job running out of memory. How would you debug & optimize it?

Explain how you’d join a huge fact table (10 TB) with a small dimension table efficiently.

How would you implement deduplication in PySpark where you keep only the latest record per ID?

Your job has frequent shuffle spills. What are possible fixes?

How do you implement exactly-once semantics in PySpark Structured Streaming?

Explain skew handling strategies (e.g., salting, skew join optimization).

Your Spark job output has inconsistent counts between runs. How would you debug?

How do you monitor Spark jobs in production? Which metrics matter?

How do you optimize PySpark code for iterative ML workloads?

Get Rahul Sounder’s stories in your inbox
Join Medium for free to get updates from this writer.

Enter your email
Subscribe
Design a pipeline in PySpark to ingest Kafka stream, enrich with dimension data, and load into Snowflake.


3. Python Classes & Objects (OOP)
   
✅ 15 Core Questions
What are classes and objects in Python? Give a simple example.

Difference between @classmethod, @staticmethod, and instance methods.

Explain inheritance in Python with example.

What is method overriding vs overloading in Python?

Difference between __init__ and __new__.

Explain multiple inheritance and MRO (Method Resolution Order).

What are abstract classes in Python?

Difference between encapsulation and abstraction.

How is polymorphism achieved in Python?

Explain the difference between composition and inheritance.

What are dataclasses in Python? When would you use them?

What is the role of super() in Python OOP?

What are magic/dunder methods in Python? Give examples.

Difference between shallow copy and deep copy in objects.

What are metaclasses in Python?

🔥 10 Complex Questions

Implement a Singleton class in Python.

Design a class for a DataPipeline that supports add_task(), run_tasks(), and logging.

Explain how you’d use OOP principles to model a Spark Job Executor.

Write a Python class to implement a custom iterator for Fibonacci numbers.

Design a plugin system using abstract classes.

You need to design a RetryableJob class for ETL jobs that retries on failure with exponential backoff. How would you do it?

Implement a DataFrameWrapper class that adds custom validation before passing to PySpark.

How would you implement dependency injection in Python OOP?

Create a base class for data connectors (e.g., MySQL, Snowflake, S3) and extend for each type.

Explain how decorators can be implemented as classes.



🔹 4. SQL

✅ 15 Core Questions

Difference between INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL OUTER JOIN.

What is the difference between WHERE and HAVING?

How do window functions work? Give examples.

What is a CTE (Common Table Expression)?

Difference between UNION and UNION ALL.

What is the difference between RANK(), DENSE_RANK(), and ROW_NUMBER()?

How do you handle NULL values in SQL joins and aggregations?

What are indexes? How do clustered vs non-clustered indexes differ?

What is normalization? Explain 1NF, 2NF, 3NF.

What is denormalization? When is it useful?

How do you detect duplicate rows in SQL?

Explain correlated vs uncorrelated subqueries.

What’s the difference between OLTP and OLAP queries?

How do you implement slowly changing dimensions (SCD) in SQL?

Explain materialized views and their use cases.

🔥 10 Complex Questions

Write a query to find the top 3 highest salaries per department.

Write a query to detect gaps in a sequence of dates for each user.

Given a sales fact table, how would you calculate rolling 7-day average sales?

Write a query to find customers who purchased in consecutive months.

Write a query to detect employees whose salary is above department average.

Write a query to pivot product sales from rows into columns dynamically.

Write a query to find the nth highest salary without using TOP or LIMIT.

Write a query to find duplicates across multiple columns and keep only the latest row.

Write a query to rank customers based on lifetime value.

Optimize a query joining a 1B row fact table with a 10M row dimension table. What techniques would you use?
