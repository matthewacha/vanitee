from flask import session, request, url_for, Blueprint, render_template, redirect

users = Blueprint('users', __name__, template_folder = 'templates')

@users.route('/')
def index():
    return redirect(url_for('users.signup'))

@users.route('/signup', methods = ['GET','POST'])
def signup():
    return render_template('signup.html', form = form, title = 'Signup')

@users.route('/login', methods = ['GET','POST'])
def login():
    return render_template('login.html', form = form, title = 'login')
