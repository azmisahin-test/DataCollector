import os
import time
import mysql.connector
from pymongo import MongoClient
import requests

def collect_data():
    # MySQL'den veri çekme
    mysql_conn = mysql.connector.connect(
        host=os.environ['MYSQL_HOST'],
        user=os.environ['MYSQL_USER'],
        password=os.environ['MYSQL_PASSWORD'],
        database=os.environ['MYSQL_DATABASE']
    )
    mysql_cursor = mysql_conn.cursor()
    mysql_cursor.execute("SELECT * FROM your_table;")
    mysql_data = mysql_cursor.fetchall()

    # MongoDB'ye veri ekleme
    mongo_client = MongoClient(os.environ['MONGO_URI'])
    mongo_db = mongo_client[os.environ['MONGO_DATABASE']]
    mongo_collection = mongo_db['your_collection']
    mongo_collection.insert_many([{'data': item} for item in mysql_data])

    # API'den veri çekme
    response = requests.get('https://api.example.com/data')
    if response.status_code == 200:
        api_data = response.json()
        mongo_collection.insert_one({'api_data': api_data})

    mysql_conn.close()

if __name__ == "__main__":
    while True:
        collect_data()
        time.sleep(int(os.environ['SLEEP_DURATION']))
