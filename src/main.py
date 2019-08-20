from app import app, db
from app.models import User,Sample, Post, Batch, Location, Result1, Result2, Study, Sample_study




@app.shell_context_processor
def make_shell_context():
    return {'db' : db, 'User':User,'Sample':Sample,'Batch':Batch,'Location':Location,'Result1':Result1,'Result2':Result2,'Sample_study':Sample_study,'Study':Study,'Post' : Post}
if __name__ == "__main__":
     
    app.run(debug=True)