import os
import mysql.connector
from mysql.connector import Error

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME'),
            port=int(os.getenv('DB_PORT', 3306))  # Default to 3306 if not set
        )

        if connection.is_connected():
            return connection
        else:
            return {"status": "error", "message": "Failed to connect to the database"}

    except Error as e:
        return {"status": "error", "message": f"Database connection error: {e}"}

    finally:
        if 'connection' in locals() and connection.is_connected():
            connection.close()
