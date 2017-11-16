from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
db.create_all()

from app import models
from app.users.views import users as users_blueprint
app.register_blueprint(users_blueprint)
"""
from app.posts import posts as posts_blueprint
app.register_blueprint(posts_blueprint)

"""

if __name__=='__main__':
    __init__.main()
