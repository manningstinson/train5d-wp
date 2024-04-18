from flask import Flask, render_template

app = Flask(__name__)

@app.route('/retrieve_exercise')
def retrieve_exercise():
    return render_template('retrieve-exercise.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
