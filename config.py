import os#pragma:no cover
DEBUGING = True
BASEDIR = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, 'db.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
