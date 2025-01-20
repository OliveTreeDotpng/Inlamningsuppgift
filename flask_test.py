from flask import Flask, redirect, url_for, render_template, request
#import bcrypt

app = Flask(__name__)

@app.route("/")
def home():
    success = request.args.get("success") # Hämta success från URL:en
    return render_template("index.html", success = success)

@app.route("/add", methods=["POST"])
def add():
    service = request.form.get("service")
    password = request.form.get("password")
    return redirect(url_for("home", success="true"))
    


#@app.route("/get", methods=["POST"])


if __name__ == "__main__":
    app.run()