from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm, SignupForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': "Employee"}

    return render_template('index.html', title='Home', user=user)


# POST - request to sent information to client/server
# GET - retrive information from client/server
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    # vaildate login form
    if form.validate_on_submit():
        # display sucessful login message
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('skills'))

    return render_template('login.html', title='Sign In', form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    # vaildate signup form
    if form.validate_on_submit():
        # display sucessful sign up message
        flash('{} has signed up using email {} and password {}'.format(
            form.username.data, form.email.data, form.password.data))
        return redirect(url_for('index'))
    
    return render_template('signup.html', title='Sign Up', form=form)


@app.route('/skills', methods=['GET', 'POST'])
def skills():
    return render_template('skills.html', title='Skills page')