from flask import render_template, session, redirect, url_for
import json
from flask import request
import codecs
from . import main
from .. import db
from ..models import Poem


@main.route('/')
def index():
    return render_template('start.html')

@main.route('/home')
def home():
    return render_template('index.html')


@main.route('/poems')
def poems():
    return render_template('poemlist.html')


@main.route('/poems/<title>')
def poem(title):
    return render_template('poem.html', title=title)

@main.route('/search', methods=['POST'])
def search():
    keyword = request.form['keyword']
    searchOption = int(request.form.getlist('searchOption')[0])
    print(searchOption)
    reader = codecs.getreader("utf-8")
    with main.open_resource('static/poems.json') as data_file:    
        data = json.load(reader(data_file))
    poemField = ['author','title','poem']
    dataHit = list(filter(lambda poem: keyword in poem[poemField[searchOption]] ,data))
    return render_template('search.html', data = dataHit)

# @main.route('/create')
# def create():
#     p = Poem(
#         title = '你好',
#         content = "dfdd",
#         author = "asdf",
#         category = "asdf"
#     )
#     db.session.add(p)
#     db.session.commit()
#     return "insert"

# @main.route('/showdb')
# def showdb():
#     p = Poem.query.all()[-1].title
#     return "insert" + p