from flask import Flask, render_template, request
app = Flask(__name__)
app.debug = True

@app.route('/', methods=['GET'])
def dropdown():
    colours = ['Sample', 'Batch', 'Study', 'Location', 'Result1', 'Result2' ]
    return render_template('test.html', colours=colours)

if __name__=="__main__":
    app.run

    from flask import Flask, render_template, url_for, request, redirect 


    application = Flask(__name__)
    
    def get_add_data(month):
        data = {
            "Sample",
            "Batch",
            "Location": "Third month of the year",
            "April": "Fourth month of the year",
            "May": "Fifth month of the year"        
        }
        return data.get(month, "Data is not found").strip()
    
    @application.route('/', methods=['GET', 'POST'])
    def home():
        if request.method == "POST":
            month = request.form.get('month')
            return render_template('home.html', data = get_monthly_data(month))
        return render_template('home.html')
    def get_data(seqbox):
        data = {
            "Sample",
            "Batch",
            "Location",
            "Result1",
            "Result2",
            "Study",
            "Sample_study"      
        }
        return data.get(month, "Data is not found").strip()
    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == "POST":
            seqbox = request.form.get('seqbox')
            return render_template('index.html', data = get_data(seqbox))
    if __name__ == '__main__':
        application.run(debug = True)