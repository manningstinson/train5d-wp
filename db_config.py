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
        database_url = DBConfig.get_database_url()
        ssl_mode = "REQUIRED"  # Change this to match your SSL mode
        
        # Append SSL parameters to the connection URL
        if "ssl" not in database_url.lower():
            database_url += "?ssl=" + ssl_mode
        else:
            database_url += "&ssl=" + ssl_mode

        return create_engine(database_url, connect_args={'ssl': {'ssl_mode': ssl_mode}})