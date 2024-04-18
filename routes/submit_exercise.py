from flask import Flask, render_template

app = Flask(__name__)

@app.route('/submit_exercise')
def submit_exercise():
    return render_template('submit-exercise.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
