from app import app, db
from app.models import Sample, Post




@app.shell_context_processor
def make_shell_context():
    return {'db' : db, 'User':User,'Sample':Sample,'Batch':Batch,'Location':Location,'Result1':Result1,'Result2':Result2,'Sample':Sample,'Sample_study':Sample_study,'Study':Study,'Post' : Post}
    
