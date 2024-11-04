from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Card')
def left_sidebar():
    return render_template('Card.html')


if __name__ == '__main__':
    app.run(debug=True)
