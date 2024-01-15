import os
from flask import Flask
from flask import jsonify
from flask import render_template

app = Flask(__name__)

APP_NAME = os.getenv('APP_NAME')
APP_COLOR = os.getenv('APP_COLOR')

@app.route('/')
def index():
    return render_template('index.html', app_name=APP_NAME, app_color=APP_COLOR)

@app.route('/health')
def health():
    return jsonify({'status': 'UP', 'color': APP_COLOR}), 200

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=80
    )
