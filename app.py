from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/time')
def get_current_time():
    return f"Current Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

if __name__ == '__main__':
    app.run(debug=True)
