from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<p>Hello, World!</p>'

@app.route('/time')
def get_current_time():
    return f"<p>Current Time: <strong>{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</strong></p>"

if __name__ == '__main__':
    app.run(debug=True)
