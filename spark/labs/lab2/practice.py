from pyspark import SparkContext
from pyspark.sql import SparkSession

context = SparkContext()
spark = SparkSession(context)

df = spark.read \
    .format('csv') \
    .option('header', 'true') \
    .option('inferSchema', 'true') \
    .load('C:\\Users\\yelad\\PycharmProjects\\m2i\\data\\hr\\employees.csv')

print(df.count())

df.printSchema()