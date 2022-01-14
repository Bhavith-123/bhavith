from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<html><body><h3 style='color:blue;'><b>WELCOME TO KB WEB SERVICES</b></h3></body></html>"
