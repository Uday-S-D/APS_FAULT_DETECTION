import pymongo
import pandas as pd
import json

from sensor.config import mongo_client


# Provide the mongodb localhost url to connect python to mongodb.
#client = pymongo.MongoClient("mongodb+srv://usd:a123$@cluster0.ucvqpvy.mongodb.net/?retryWrites=true&w=majority")

DATA_FILE_PATH = "/config/workspace/aps_failure_training_set1.csv"
DATABASE_NAME = 'aps'
COLLECTION_NAME = 'sensor'

if __name__ == '__main__':
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and Columns:{df.shape}")

#Convert dataframe to json so that we can dump these record in mongo db
df.reset_index(drop=True,inplace=True)

json_record = list(json.loads(df.T.to_json()).values())
print(json_record[0])


#Insert Converted record to MongoDb
mongo_client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)