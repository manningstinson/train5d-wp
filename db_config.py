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
    ssl_mode = "verify-ca"  # Use the desired SSL mode

    # Use connect_args for dialect-specific arguments (assuming MySQL)
    engine = create_engine(database_url, connect_args={'sslmode': ssl_mode})
    return engine

engine = DBConfig.create_engine()
