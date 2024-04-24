from sqlalchemy import create_engine
import os

class DBConfig:
    @staticmethod
    def create_engine():
        """
        Creates a SQLAlchemy engine using environment variables for configuration.
        """
        url = os.getenv('MYSQL_DATABASE_URL')
        ssl_mode = os.getenv('MYSQL_SSL_MODE')
        engine = create_engine(url, connect_args={'sslmode': ssl_mode} if ssl_mode else None)
        return engine