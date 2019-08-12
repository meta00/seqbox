from flask import Flask, render_template, url_for, request, redirect 


app = Flask(__name__)

def get_monthly_data(month):
    data = {
        "January": "First month of the year",
        "February": "Second month of the year",
        "March": "Third month of the year",
        "April": "Fourth month of the year",
        "May": "Fifth month of the year"        
    }
    return data.get(month, "Data is not found").strip()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        month = request.form.get('month')
        return render_template('home.html', data = get_monthly_data(month))
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug = True)
   
@app.route('/user/<username>')
def show_user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('show_user.html', user=user)