from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import _moment

app = Flask(__name__)

bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/poems')
def poems():
    return render_template('poems.html')

@app.route('/poems/<name>')
def poem(name):
    return '<h1>Hello, %s</h1>' %name

@app.route('/poets')
def poets():
    pass

@app.route('/poets/<name>')
def poet():
    pass

if __name__ == '__main__':
    app.run(debug=True)