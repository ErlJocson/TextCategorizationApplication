import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv(
    dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env')
)

def get_db_connection():

    return mysql.connector.connect(
        host = os.get("DATABASE_HOST"),
        user = os.get("DATABASE_USER"),
        password = os.get("DATABASE_PASSWORD"),
        database = os.get("DATABASE_DB")
    )
