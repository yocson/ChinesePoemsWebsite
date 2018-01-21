#coding=gbk  
from flask import render_template, session, redirect, url_for
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

@main.route('/create')
def create():
    str = "你好"
    p = Poem(
        title = unicode(str, "gbk"),
        content = "dfdd",
        author = "asdf",
        category = "asdf"
    )
    db.session.add(p)
    db.session.commit()
    return "insert"

@main.route('/showdb')
def showdb():
    p = Poem.query.all()[1].title
    return "insert" + p