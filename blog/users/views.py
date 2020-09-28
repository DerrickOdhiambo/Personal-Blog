from flask import render_template, flash, url_for, redirect
from blog.users.forms import LoginForm, RegistrationForm
from . import users


@users.route('/registration', methods=['GET', 'POST'])
def register():
  form = RegistrationForm()
  if form.validate_on_submit():
    flash(f'Account for {form.username.data} has been created successfully!', 'success')
    return redirect(url_for('main.home'))
  return render_template('register.html', title = 'Register', form = form)


@users.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
  return redirect(url_for('main.home'))
  return render_template('login.html', title = 'Login', form = form)

