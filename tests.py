import unittest
import os
from flask import url_for
from config import config, environments
from app import app, db, models
#import images

class ConfigTest(unittest.TestCase):
    """ This module sets up test udsers, bucketlistsand items used for testing the system """
    def create_app(self):
        """ create the flask application with testing configurations """
        app.config.from_object(config.environment_configuration['testing'])
        return app

    def setUp(self):
        """ create test database and client """
        self.basedir = os.path.abspath(os.path.dirname(__file__))
        app = self.create_app()
        self.client = app.test_client()
        SECRET_KEY = app.config.get("SECRET_KEY")
        db.create_all()

    def test_testing_config(self):
        self.assertTrue(environments.basedir == self.basedir)
        self.assertTrue(app.config['DEBUG'])
        self.assertTrue(app.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///' + os.path.join(self.basedir, 'db/testing.db'))
        self.assertFalse(app.config['SQLALCHEMY_TRACK_MODIFICATIONS'])

    def tearDown(self):
        """ Drop the database after every test """
        db.drop_all()

if __name__ == '__main__':
    unittest.main()
