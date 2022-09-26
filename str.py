from pyspark.sql import SparkSession



if __name__ == "__main__":
       spark = SparkSession.builder.appName("Streaming").getOrCreate()
       
       jsonschema = "nome STRING, postagem STRING, data INT"
       
       df = spark.readStream.json("/home/pc/teste_Streaming/", schema=jsonschema)
       
       diretorio = "/home/pc/temp/"
       stcal = df.writeStream.format("console").outputMode("append").trigger(processingTime="5 second").option("checkpointlocation", diretorio).start()
       
       stcal.awaitTermination()
