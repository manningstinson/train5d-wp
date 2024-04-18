from flask import Flask, render_template
from routes.submit_exercise import submit_exercise
from routes.retrieve_exercise import retrieve_exercise

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_exercise')
def submit():
    return render_template('submit-exercise.html')

@app.route('/retrieve_exercise')
def retrieve():
    return render_template('retrieve-exercise.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)