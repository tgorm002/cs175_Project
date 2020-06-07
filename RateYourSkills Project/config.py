import os


class Config(object):
    # create secret key for use with flask-wtf
    # protects web forms against Cross-Site Request Forgery
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'