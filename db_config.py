import os
from sqlalchemy import create_engine

class DBConfig:
    @staticmethod
    def get_database_url():
        database_url = os.getenv('DATABASE_URL')
        if not database_url:
            raise ValueError("DATABASE_URL environment variable is not set")
        return database_url

    @staticmethod
    def create_engine():
        database_url = DBConfig.get_database_url()
        ssl_mode = "allow"  # Change this to match your SSL mode if needed

        engine = create_engine(database_url, connect_args={'sslmode': ssl_mode})
        return engine

engine = DBConfig.create_engine()