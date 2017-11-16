import unittest
import os
from flask import url_for
import config
from app import app, db, models
#import images
class ConfigTest(unittest.TestCase):
    def test_config(self):
        self.assertTrue(config.BASEDIR == os.path.abspath(os.path.dirname(__file__)))
        self.assertTrue(config.DEBUGING)
        BASEDIR = os.path.abspath(os.path.dirname(__file__))
        self.assertTrue(config.SQLALCHEMY_DATABASE_URI == 'sqlite:///' + os.path.join(BASEDIR, 'db.db'))
        self.assertFalse(config.SQLALCHEMY_TRACK_MODIFICATIONS)

class TestModels(unittest.TestCase):
    def test_user_class(self):
        model = models.User('King', 'Arthur', 'em@gmail.com','amazing')
        self.assertEqual(model.first_name, 'King')
        self.assertEqual(model.__repr__(), 'King Arthur')
        
class UsersTests(unittest.TestCase):
    def test_index_page(self):
        self.testing = app.test_client(self)
        response = self.testing.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Vanitee', response.data)
"""
        ###############
        ##TEST SIGNUP##
        ###############
    def test_signup_page_works(self):
        self.testing = app.test_client(self)
        response = self.testing.post('/signup', data = dict(first_name = 'Lex',
                                                       last_name = 'Luthor',
                                                       email = 'lex@gmail.com',
                                                       password = 'winner'),
                                follow_redirects = True)
        self.assertIn('Login to confirm your vanitee', response.data)
        self.assertEqual(response.status, 200,"you shouild get an error 200!")

    def test_invalid_signup(self):
        #user already exists
        self.testing = app.test_client(self)
        self.testing.post('/signup', data = dict(first_name = 'Lex',
                                                       last_name = 'Luthor',
                                                       email = 'lex@gmail.com',
                                                       password = 'winner'),
                                follow_redirects = True)
        response = self.testing.post('/signup', data = dict(first_name = 'Lex',
                                                       last_name = 'Luthor',
                                                       email = 'lex@gmail.com',
                                                       password = 'winner'),
                                follow_redirects = True)
        self.assertIn('User already taken', response.data)
        self.assertEqual(response.status_code, 401)

        ##############
        ##TEST LOGIN##
        ##############

    def test_login_page(self):
        self.testing = app.test_client(self)
        self.testing.post('/signup', data = dict(first_name = 'Lanyero',
                                                       last_name = 'Amsell',
                                                       email = 'lam@gmail.com',
                                                       password = 'winners12'),
                                follow_redirects = True)
        response = self.testing.post('/login', data = dict(email='lam@gmail.com',password='winners12'),
                                follow_redirects = True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Welcome to Vanitee', response.data)
        
    def test_invalid_login_password(self):
        #Wrong Password
        self.testing = app.test_client(self)
        self.testing.post('/signup', data = dict(first_name = 'emma',
                                                       last_name = 'Amanya',
                                                       email = 'ame@gmail.com',
                                                       password = 'winner'),
                                follow_redirects = True)
        response = self.testing.post('/login', data = dict(email='ame@gmail.com',password='winners12'),
                                follow_redirects = True)
        self.assertEqual(response.status_code, 401)
        self.assertIn('Wrong password', response.data)

    def test_invalid_login_user(self):
        #Wrong email
        self.testing = app.test_client(self)
        self.testing.post('/signup', data = dict(first_name = 'emma',
                                                       last_name = 'Amanya',
                                                       email = 'ame@gmail.com',
                                                       password = 'winner'),
                                follow_redirects = True)
        response = self.testing.post('/login', data = dict(email = 'amelek@gmail.com',
                                                      password = 'winner'),
                                follow_redirects = True)
        self.assertIn('Wrong email', response.data)


    ###############
    ##TEST LOGOUT##
    ###############
    def test_invalid_logout(self):
        #Not logged in
        self.testing = app.test_client(self)
        result = self.testing.post('/logout', follow_redirects = True)
        self.assertIn('You must be logged in to logout', result.data)
        
    def test_valid_logout(self):
        #logged in
        self.testing = app.test_client(self)
        self.testing.post('/signup', data = dict(first_name = 'Edward',
                                                       last_name = 'King',
                                                       email = 'king@gmail.com',
                                                       password = 'winners12'),
                                follow_redirects = True)
        self.testing.post('/login', data = dict(email='king@gmail.com',password='winners12'),
                                follow_redirects = True)
        result = self.testing.post('/logout', follow_redirects = True)
        self.assertIn('Please log in again to use vanitee', result.data)

    #####################
    ##TEST USER PROFILE##
    #####################
    def test_profile_page(self):
        self.testing = app.test_client(self)
        self.testing.post('/signup', data = dict(first_name = 'Edward',
                                                       last_name = 'King',
                                                       email = 'king@gmail.com',
                                                       password = 'winners12'),
                                follow_redirects = True)
        self.testing.post('/login', data = dict(email='lam@gmail.com',password='winners12'),
                                follow_redirects = True)
        response = self.testing.get('/profile',follow_redirects = True)
        self.assertEqual(response.data, 200)
        self.assertIn('Edward King', response.data)
        self.assertIn('hobbies', response.data)

    def test_edit_profile(self):
        self.testing = app.test_client(self)
        self.testing.post('/signup', data = dict(first_name = 'Elsa',
                                                       last_name = 'Queen',
                                                       email = 'ella@gmail.com',
                                                       password = 'winners12'),
                                follow_redirects = True)
        self.testing.post('/login', data = dict(email='ella@gmail.com',password='winners12'),
                                follow_redirects = True)
        self.testing.get('/profile',follow_redirects = True)
        response = self.testing.post('/profile/edit', data = dict(first_name = 'Eliza',
                                                            last_name = 'Jonsons',
                                                            hobbies = "'joggin','swimming', 'shopping'"
                                                            ),
                               follow_redirects = True)
        self.assertEqual(response.data, 200)
        self.assertIn('shopping', response.data)
        self.assertIn("'joggin','swimming', 'shopping'", response.data)
        self.assertIn('Eliza', response.data)

    ####################
    ##TEST POSTS##
    ####################
    def test_show_no_posts(self):
        self.testing = app.test_client(self)
        self.testing.post('/signup', data = dict(first_name = 'Lord',
                                                       last_name = 'Lancaster',
                                                       email = 'lord@gmail.com',
                                                       password = 'winners12'),
                                follow_redirects = True)
        self.testing.post('/login', data = dict(email='lord@gmail.com',password='winners12'),
                                follow_redirects = True)
        result = self.testing.get('/dashboard',
                     follow_redirects=True)
        self.assertIn('No posts by you', result.data)

    def test_show_recent_posts(self):
        self.testing = app.test_client(self)
        self.testing.post('/signup', data = dict(first_name = 'Lord',
                                                       last_name = 'Lancaster',
                                                       email = 'lord@gmail.com',
                                                       password = 'winners12'),
                                follow_redirects = True)
        self.testing.post('/login', data = dict(email='lord@gmail.com',password='winners12'),
                                follow_redirects = True)
        self.testing.post('/posts/add', data = dict(img = '', tag = 'Awesome shoes'),
                          follow_redirects = True)
        self.testing.post('/posts/add', data = dict(img = '', tag = 'Me want some of these!'),
                          follow_redirects = True)
        self.testing.post('/posts/add', data = dict(img = '', tag = 'Cla$$ for sure!'),
                          follow_redirects = True)
        
        result = self.testing.get('/posts/dashboard',
                     follow_redirects = True)
        
        self.assertIn('Cla$$ for sure', result.data)

    def test_add_post(self):
        self.testing = app.test_client(self)
        self.testing.post('/signup', data = dict(first_name = 'Lois',
                                                       last_name = 'Admatha',
                                                       email = 'lois@gmail.com',
                                                       password = 'winners12'),
                                follow_redirects = True)
        self.testing.post('/login', data = dict(email='lois@gmail.com',password='winners12'),
                                follow_redirects = True)
        response = self.testing.post('/posts/add', data = dict(img = '', tag = 'Awesome shoes'),
                          follow_redirects = True)
        self.assertEqual(response.status_code, 200)
        self.asserIn('Awesome shoes', response.data)

    def test_edit_post(self):
        self.testing = app.test_client(self)
        self.testing.post('/signup', data = dict(first_name = 'Lanister',
                                                       last_name = 'Admatha',
                                                       email = 'lani@gmail.com',
                                                       password = 'winners12'),
                                follow_redirects = True)
        self.testing.post('/login', data = dict(email='lani@gmail.com',password='winners12'),
                                follow_redirects = True)
        self.testing.post('/posts/add', data = dict(img = '', tag = 'Awesome shoes'),
                          follow_redirects = True)
        response = self.testing.post('/posts/edit/<post_id>', data = dict(post_id = 1, tag = 'Just enghh!'),
                                     follow_redirects = True)
        self.assertIn('Just enghh', response.data)

"""
if __name__ == '__main__':
    unittest.main()
