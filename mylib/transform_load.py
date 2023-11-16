from pyspark.sql import SparkSession
from pyspark.sql.functions import monotonically_increasing_id

def load(dataset="dbfs:/FileStore/tables/individual_project3/wc_20140609_140000.csv", 
         dataset2="dbfs:/FileStore/tables/individual_project3/wc_20140613_205820.csv"):
    spark = SparkSession.builder.appName("Read CSV").getOrCreate()
    # load csv and transform it by inferring schema 
    event_times_df = spark.read.csv(dataset, header=True, inferSchema=True)
    serve_times_df = spark.read.csv(dataset2, header=True, inferSchema=True)

    # add unique IDs to the DataFrames
    event_times_df = event_times_df.withColumn("id", monotonically_increasing_id())
    serve_times_df = serve_times_df.withColumn("id", monotonically_increasing_id())

    # transform into a delta lakes table and store it 
    serve_times_df.write.format("delta").mode("overwrite").saveAsTable("wc609_delta")
    event_times_df.write.format("delta").mode("overwrite").saveAsTable("wc613_delta")
    
    num_rows = serve_times_df.count()
    print(num_rows)
    num_rows = event_times_df.count()
    print(num_rows)
    
    return "finished transform and load"

if __name__ == "__main__":
    load()