# Vanitee
Everything is vanitee!!

Table of contents
=================
* Introduction
* setup
* Run app
* requirements


INTRODUCTION
============
If you like it, and find it irresistable, just snap, price tag and share it to all your friends;
and the rest of the world. 


SETUP
=====
This the production stage and all hands are welcome.
For software developers to use you will need the following pre-installed:
* python 2.7
* pip 9.0.1
* Node.js

## Clone the repo

        $ git clone https://github.com/matthewacha/vanitee.git

## Clone thr repo

        $ git clone https://github.com/matthewacha/vanitee.git

## Clone thr repo

        $ git clone https://github.com/matthewacha/vanitee.git

## Clone thr repo

        $ git clone https://github.com/matthewacha/vanitee.git

RUN APP
=======
* prepare virtual environment
  (with virtualenv you get pip, we'll use it soon to install requirements):

        $ cd vanitee
        $ virtualenv --python=python2.7 venv
        $ source venv/bin/activate

* install requirements (Flask, ...) into virtualenv:

        $ pip install -r requirements.txt

* create database tables

        $ python manage.py init
        $ python manage.py migrate

* installing bower materialize and font awesome components

        $ cd app
        $ npm install --save materialize-social
        $ bower install --save materialize-social

* run development server:

        $ ./manage.py runserver

The site should now be running at `http://localhost:5000


## run tests:

* For python code:

        $ coverage run tests.py

for javascript:

        $ node tests.js

check coverage:

        $ istanbul cover tests.js
        