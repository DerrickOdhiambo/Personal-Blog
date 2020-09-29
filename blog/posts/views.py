from flask import render_template,url_for,flash, redirect, request, abort
from flask_login import current_user, login_required
from blog import db
from . import posts
from blog.models import Post, Comments, Email
from blog.posts.forms import PostForm, CommentForm
from ..email import mail_message
from blog.main.forms import EmailSubscriptionForm



@posts.route('/post/new', methods={'GET','POST'})
@login_required
def new_post():
  form = PostForm()
  if form.validate_on_submit():
    post = Post(title = form.title.data, content = form.content.data, author = current_user)
    db.session.add(post)
    db.session.commit()
    flash('Your blog-post has been created!', 'success')
    return redirect(url_for('main.home'))
  return render_template('create_post.html', title = 'Blog-Post', form = form, legend='New Blog-post')


@posts.route('/post/<int:post_id>', methods=['GET', 'POST'])
def post(post_id):
  post = Post.query.get_or_404(post_id)
  form = CommentForm()
  comments = Comments.query.filter_by(post_id=post.id).order_by(Comments.time_posted.desc()).all()
  if request.method == 'POST':
    comment = Comments(name = form.name.data, email=form.email.data, message=form.message.data, post_id=post.id)
    db.session.add(comment)
    # post.comment += 1
    flash('Your comment has been submitted!', 'success')
    return redirect(url_for('posts.post', post_id=post.id))
  return render_template('post.html', title = post.title, post=post, form=form, comments=comments)


@posts.route('/post/<int:post_id>/update', methods=['GET','POST'])
@login_required
def update_post(post_id):
  post = Post.query.get(post_id)
  if post.author != current_user:
    abort(403)
  form = PostForm()
  if form.validate_on_submit():
    post.title = form.title.data
    post.content = form.content.data
    db.session.commit()
    flash('Your blog-post has been updated!', 'success')
    return redirect(url_for('posts.post', post_id=post.id))
  elif request.method == 'GET':
    form.title.data = post.title
    form.content.data = post.content
  return render_template('create_post.html', title='Update Post', form=form, legend='Update Blog Post')


@posts.route('/post/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
  post = Post.query.get(post_id)
  if post.author != current_user:
    abort(403)
  db.session.delete(post)
  db.session.commit()
  flash('Your post has been deleted!', 'success')
  return redirect(url_for('main.home'))

@posts.route('/', methods=['GET', 'POST'])
def send_email():
  form = EmailSubscriptionForm()
  if request.method == 'POST':
    subscription_email = Email(email=form.email.data)
    db.session.add(subscription_email)
    db.session.commit()
    flash('You have succesfully subscribed to the blog post')
    return redirect(request.url)
  return render_template('home.html', form=form)
