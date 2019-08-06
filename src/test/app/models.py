from datetime import datetime
from app import db, login
from flask_login import UserMixin
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)

class Sample(db.Model):

    id_sample = db.Column(db.VARCHAR(20),primary_key=True)
    num_seq = db.Column(db.VARCHAR(60))
    date_time =db.Column(db.DATETIME)
    organism = db.Column(db.VARCHAR(30)) 
    batch = db.Column(db.VARCHAR(50),db.ForeignKey('id_batch'))
    location = db.Column(db.VARCHAR(50), db.ForeignKey('id_location'))
    path_r1 = db.Column(db.VARCHAR(40))
    path_r2 = db.Column(db.VARCHAR(40))
    result1 = db.Column(db.Integer, db.ForeignKey('id_result1'))
    result2 = db.Column(db.Integer, db.ForeignKey('id_result2'))
    #child = db.relationship('Child', backref='author', lazy='dynamic')
    
    def __repr__(self):
        return '<Sample {}>'.format(self.num_seq)


class Batch(db.Model):
    id_batch = db.Column(db.VARCHAR(30),primary_key=True)
    name_batch = db.Column(db.VARCHAR(50))
    date_batch = db.Column(db.DATE)
    instrument = db.Column(db.VARCHAR(250))
    primer = db.Column(db.VARCHAR(100))

    def __repr__(self):
        return '<Batch {}>'.format(self.name_batch)

class Location(db.Model):
    id_location = db.Column(db.VARCHAR(25),primary_key=True)
    continent = db.Column(db.VARCHAR(80))
    country  = db.Column(db.VARCHAR(60))
    province = db.Column(db.VARCHAR(40))
    city = db.Column(db.VARCHAR(50))

    def __repr__(self):
        return '<Location {}>'.format(self.continent)

class Result1(db.Model):
    id_result1 = db.Column(db.Integer,primary_key=True)
    qc = db.Column(db.VARCHAR(60))
    ql = db.Column(db.VARCHAR(60))
    description = db.Column(db.VARCHAR(250))
    snapper_variants = db.Column(db.Integer)
    snapper_ignored = db.Column(db.Integer)
    num_heterozygous = db.Column(db.Integer)
    mean_depth = db.Column(db.double)
    coverage = db.Column(db.double)
    def __repr__(self):
        return '<Result1 {}>'.format(self.qc)

class Result2(db.Model):
    
    id_result2 = db.Column(db.Integer, primary_key=True)
    mykrobe_version = db.Column(db.varchar(50))
    phylo_grp = db.Column(db.varchar(60))
    phylo_grp_covg = db.Column(db.double)
    phylo_grp_depth = db.Column(db.double)
    species = db.Column(db.varchar(50))
    species_covg = db.Column(db.double)
    species_depth = db.Column(db.double)
    lineage = db.Column(db.varchar(50))
    lineage_covg = db.Column(db.double)
    lineage_depth = db.Column(db.double)
    susceptibility = db.Column(db.varchar(50))
    variants = db.Column(db.varchar(80))
    genes = db.Column(db.varchar(100))
    drug = db.Column(db.varchar(90))
    
    def __repr__(self):
        return '<Result2 {}>'.format(self.mykrobe_version)
    
class Study(db.Model):
    id_study = db.Column(db.VARCHAR(50),primary_key=True)
    date_study = db.Column(db.DATE)
    result_study = db.Column(db.VARCHAR(80))
    
    def __repr__(self):
        return '<Study {}>'.format(self.date_study)

class Sample_study(db.Model):
    id_sample = db.Column(db.VARCHAR(40),primary_key = True)
    id_study = db.Column(db.VARCHAR(50),primary_key = True)
    def __repr__(self):
        return '<Sample_study {}>'.format(self.id_sample)

#class Child(db.Model):
    #id_sample = db.Column(db.VARCHAR(20),primary_key=True)
    #body = db.Column(db.String(140))
    #timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    #batch = db.Column(db.VARCHAR(50),db.ForeignKey('id_batch'))
    #location = db.Column(db.VARCHAR(50), db.ForeignKey('id_location'))
    #result1 = db.Column(db.Integer, db.ForeignKey('id_result1'))
    #result2 = db.Column(db.Integer, db.ForeignKey('id_result2'))
    #def __repr__(self):
        #return '<Child {}>'.format(self.body)
        #return '<Child {}>'.format(self.location)
        #return '<Child {}>'.format(self.result1)
        #return '<Child {}>'.format(self.result2)
