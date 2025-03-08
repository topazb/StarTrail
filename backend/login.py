from flask_login import UserMixin
import mysql.connector

class User(UserMixin):
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

    @staticmethod
    def get(user_id):
        # Connect to DB and get user info (this can be adjusted based on your actual DB setup)
        connection = mysql.connector.connect(
            host='your-db-host',
            user='your-db-user',
            password='your-db-password',
            database='your-db-name'
        )
        cursor = connection.cursor(dictionary=True)
        cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
        user_data = cursor.fetchone()
        if user_data:
            return User(user_data['id'], user_data['name'], user_data['email'])
        return None
