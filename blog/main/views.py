from flask import render_template
from . import main

@main.route('/')
def home():
  return render_template('home.html', title = 'Home')

@main.route('/about')
def about():
  return render_template('about.html', title = 'About')

@main.route('/articles')
def articles():
  return render_template('articles.html', title = 'Articles')