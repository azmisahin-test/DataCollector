import mysql.connector
import time
import os

MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")
MYSQL_HOST = os.getenv("MYSQL_HOST", "mysql")

def collect_data():
    # Connect to MySQL
    connection = mysql.connector.connect(
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        host=MYSQL_HOST,
        database=MYSQL_DATABASE
    )
    
    cursor = connection.cursor()
    # Insert sample data
    cursor.execute("INSERT INTO sample_data (data) VALUES ('Sample data')")
    connection.commit()
    print("Data collected and inserted.")
    cursor.close()
    connection.close()

if __name__ == "__main__":
    while True:
        collect_data()
        time.sleep(5)  # Adjust as necessary
