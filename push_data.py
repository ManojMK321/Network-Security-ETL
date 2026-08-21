import pymongo
import os
import sys
import json
from dotenv import load_dotenv

load_dotenv()

MONGO_DB_URL=os.getenv('MONGO_DB_URL')

import certifi # This will return the path to the CA certificates file.
ca=certifi.where() #  this will provide the root certificates for the SSL connection  
# ca -->certificate authority

import pandas as pd 
import numpy as numpy

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging


class NetworkDataExtract(): #etl function
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)

    def csv_to_json_convertor(self,file_path):
        try:
            data=pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            records=list(json.loads(data.T.to_json()).values()) #json.loads() converts the string to json object #.values() returns the values #data.T.to_json() converts the dataframe to json string and T->Transpose
            return records 
        except Exception as e:
            raise NetworkSecurityException(e,sys)

    def insert_data_mongodb(self,records,database,collection):
        try:
            self.database=database
            self.collection=collection
            self.records=records

            self.mongo_client = pymongo.MongoClient(
                MONGO_DB_URL,
                tls=True,
                tlsCAFile=ca,
                serverSelectionTimeoutMS=30000
            )
            self.database=self.mongo_client[self.database]

            self.collection=self.database[self.collection]
            self.collection.insert_many(self.records)
            return(len(self.records))
        except Exception as e:
            raise NetworkSecurityException(e,sys)



if __name__ == '__main__':
    FILE_PATH="Network_Data/phisingData.csv"
    DATABASE="ManojKumar"
    Collection="NetworkData"
    networkobj=NetworkDataExtract()
    records=networkobj.csv_to_json_convertor(file_path=FILE_PATH)
    print(records)
    no_of_records=networkobj.insert_data_mongodb(records,DATABASE,Collection)
    print(no_of_records)
