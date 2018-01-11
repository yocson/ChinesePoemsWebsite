from flask import render_template, session, redirect, url_for
from . import main


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/poems')
def poems():
    return render_template('poemlist.html')


@main.route('/poems/<title>')
def poem(title):
    return render_template('poem.html', title=title)