from flask import Flask
from submit_exercise import submit_exercise
from retrieve_exercise import retrieve_exercise

app = Flask(__name__)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
