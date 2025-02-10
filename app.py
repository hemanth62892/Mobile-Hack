from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/hacked')
def hacked():
    return render_template('hacked.html')

@app.route('/birthday')
def birthday():
    return render_template('birthday.html')

if __name__ == '__main__':
    app.run(debug=True)
