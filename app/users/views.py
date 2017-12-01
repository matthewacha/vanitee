from flask import session, request, url_for, Blueprint, render_template, redirect

users = Blueprint('users', __name__, template_folder = 'templates')

@users.route('/')
def index():
    return render_template('index.html', title = 'Vanitee')

@users.route('/signup', methods = ['GET','POST'])
def signup():
    if request.method=='GET':
        return render_template('signup.html', title = 'Signup')

@users.route('/login', methods = ['GET','POST'])
def login():
    # return render_template('login.html', form = form, title = 'login')
    pass
