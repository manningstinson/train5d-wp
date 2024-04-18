import os
from sqlalchemy import create_engine

class DBConfig:
    @staticmethod
    def get_database_url():
        # Assuming you're using the environment variable DATABASE_URL
        # with the format: mysql://username:password@host/dbname
        database_url = os.getenv('DATABASE_URL')
        if not database_url:
            raise ValueError("DATABASE_URL environment variable is not set")
        return database_url

    @staticmethod
    def create_engine():
        return create_engine(DBConfig.get_database_url())

# Example usage:
# engine = DBConfig.create_engine()