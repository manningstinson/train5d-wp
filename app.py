from flask import Flask, render_template
from routes.submit_exercise import submit_exercise
from routes.retrieve_exercise import retrieve_exercise
from db_config import DBConfig

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

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


@app.route('/submit_exercise')
def submit():
    return render_template('submit-exercise.html')

@app.route('/retrieve_exercise')
def retrieve():
    return render_template('retrieve-exercise.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)