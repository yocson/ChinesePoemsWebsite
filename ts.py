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
    return render_template('poemlist.html')

@app.route('/poems/<title>')
def poem(title):
    return render_template('poem.html', title=title)

@app.route('/poets')
def poets():
    pass

@app.route('/poets/<name>')
def poet():
    pass

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)