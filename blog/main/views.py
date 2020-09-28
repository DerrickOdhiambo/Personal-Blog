from flask import render_template
from . import main
from blog.models import Post

@main.route('/')
def home():
  posts = Post.query.all()
  return render_template('home.html', title = 'Home', posts=posts)

@main.route('/about')
def about():
  return render_template('about.html', title = 'About')

@main.route('/articles')
def articles():
  return render_template('articles.html', title = 'Articles')