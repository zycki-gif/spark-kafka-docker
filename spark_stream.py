from pyspark.sql import SparkSession
from pyspark.sql.types import StructType,StructField,LongType,IntegerType,FloatType,StringType
from pyspark.sql.functions import split,from_json,col


spark = SparkSession.builder.appName("KafkaStream").getOrCreate()

schema = StructType([StructField("number", IntegerType(), True)])

df = spark.readStream.format("kafka").option("kafka.bootstrap.servers", "localhost:9092").option("subscribe", "test").load()

df1 = df.selectExpr("CAST(value AS STRING)")

df1.printSchema()

