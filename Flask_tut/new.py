from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return ("Hi! This is Nihar")

@app.route("/admin")
def hello_admin():
    return ("admin is here")

app.run()