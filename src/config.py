from flask import Flask, render_template



app = Flask(__name__)

import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    """[summary]
    
    Arguments:
        object {[type]} -- [description]
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'mysql://oucru:vitrygtr@localhost/seqbox'
    SQLALCHEMY_TRACK_MODIFICATIONS = False







