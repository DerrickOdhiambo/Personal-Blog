from flask import render_template, request, redirect, flash, url_for
from . import main
from blog.models import Post
from ..request import get_quotes
from blog.main.forms import EmailSubscriptionForm
from ..models import Email
from blog import db


@main.route('/')
@main.route('/home', methods=['GET', 'POST'])
def home():
  posts = Post.query.all()
  form = EmailSubscriptionForm()
  random_quotes = get_quotes()
  if form.validate_on_submit():
    email_subscription = Email(email=form.email.data)
    db.session.add(email_subscription)
    db.session.commit()
    flash('You have successfully subscribed to blog updates', 'success')
    return redirect(url_for('main.home'))
  else:
    flash
  return render_template('home.html', title = 'Home', posts=posts, random_quotes=random_quotes, form=form)

@main.route('/about')
def about():
  return render_template('about.html', title = 'About')

