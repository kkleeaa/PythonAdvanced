import sqlite3

import os

from dotenv import load_dotenv



load_dotenv()

Database_Url = os.getenv("Database_Url")





def get_db_connection():

    connection = sqlite3.connect(Database_Url)

    connection.row_factory = sqlite3.Row

    return connection
