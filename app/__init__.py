from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import config

# create the flask application
def create_application(environment):
    app = Flask(__name__)
    app.config.from_object(config.environment_configuration[environment])
    return app

app = create_application("development")
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import models
from app.users.views import users as users_blueprint
app.register_blueprint(users_blueprint)

if __name__=='__main__':
    __init__.main()
