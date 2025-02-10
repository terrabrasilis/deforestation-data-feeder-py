import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

host = os.getenv('DB_HOST')
database = os.getenv('DB_NAME')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
port = os.getenv('DB_PORT')

def connect_db():    
    conn = psycopg2.connect(
        dbname = database,
        user = user,
        password = password,
        host = host,
        port = port
    )
    return conn
    
def execute_query(select_query):
    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute(select_query)
        data = cur.fetchall()
        cur.close()
        return data
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        