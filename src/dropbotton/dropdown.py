from flask import Flask, render_template, request
app = Flask(__name__)
app.debug = True

@app.route('/', methods=['GET'])
def dropdown():
    colours = ['Sample', 'Batch', 'Study', 'Location', 'Result1', 'Result2' ]
    return render_template('test.html', colours=colours)

if __name__=="__main__":
    app.run