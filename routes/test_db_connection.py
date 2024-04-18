from flask import render_template
from db_config import DBConfig

def register_routes(app):
    @app.route('/test_db_connection')
    def test_db_connection():
        try:
            # Create SQLAlchemy engine using DBConfig
            engine = DBConfig.create_engine()
            connection = engine.connect()

            # Example query
            result = connection.execute("SELECT * FROM ex_list LIMIT 1")
            row = result.fetchone()

            connection.close()

            # Return the fetched row as a string
            return str(row)

        except Exception as e:
            return "Error: " + str(e)

