from flask import Flask, render_template
from flask_frozen import Freezer

app = Flask(__name__)
freezer = Freezer(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Card')
def left_sidebar():
    return render_template('Card.html')

if __name__ == '__main__':
    freezer.freeze()