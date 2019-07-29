from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) 
app.config['DEBUG'] = True


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:vitrygtr@localhost:3306/seqbox'
SQLALCHEMY_TRACK_MODIFICATIONS = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    email = db.Column(db.String(75)) 
    username = db.Column(db.String(50)) 
    password = db.Column(db.String(100)) 


@app.route('/') 
def home(): 
    return render_template('home.html', title='Home') 
    
if __name__ == '__main__': 
    app.run()