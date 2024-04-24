import os
import mysql.connector

class DBConfig:
    @staticmethod
    def create_connection():
        """
        Creates a MySQL connection using environment variables for configuration.
        """
        connection = mysql.connector.connect(
            user=os.getenv('MYSQL_USER'),
            password=os.getenv('MYSQL_PASSWORD'),
            host=os.getenv('MYSQL_HOST'),
            port=os.getenv('MYSQL_PORT', '3306'),
            database=os.getenv('MYSQL_DATABASE'),
            ssl_mode=os.getenv('MYSQL_SSL_MODE')
        )
        return connection