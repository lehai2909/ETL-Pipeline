from pyspark.sql import SparkSession
from pyspark.sql.types import *
import pandas as pd


spark = SparkSession.builder.getOrCreate()
table = spark.read.csv('log/log-20210430.csv',header = True, sep=',')
schema = table.schema
#table.withColumnRenamed("jsonPayload.message","message").select("insertId","timestamp","message")

streaming_table = spark.readStream.option("maxFilesPerTrigger",1).schema(schema).csv('log',header = True)

query = streaming_table.withColumnRenamed("jsonPayload.message","message").select("insertId","timestamp","message")\
	.writeStream.format('console').outputMode('update').start()

query.awaitTermination()
