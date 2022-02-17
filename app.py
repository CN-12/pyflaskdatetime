from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def time():
    date = datetime.now()
    return date.strftime("%Y-%m-%d")

@app.route('/time')
def times():
    while True:
        date = datetime.now()
        return date.strftime("%H:%M:%S")


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000', debug=True)