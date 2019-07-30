from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route("/blog/<int:id>")
def show_blog(id):
    return ("Blog number: %d" %id)

@app.route("/admin")
def hello_admin():
    return ("Hello admin")
    
@app.route("/user/<name>")
def hello_username(name):
    return ("Hello %s" %name)

@app.route("/<name>")
def hello_user(name):
    if name == "admin":
        return redirect(url_for("hello_admin"))
    elif name == "guest":
        return redirect(url_for("hello_guest"))
    else:
        return redirect(url_for("hello_username"))

@app.route("/guest")
def hello_guest():
    return("Hello guest")
if __name__ == '__main__':
   app.run(debug=True)