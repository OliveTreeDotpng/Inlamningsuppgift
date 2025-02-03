from flask import redirect, url_for, render_template, request, flash
from werkzeug.security import check_password_hash, generate_password_hash 
from app.models import db, Account # Importera db och Account från models.py
from flask import current_app as app # Importera app från __init__.py

@app.route("/")
def home():
    success = request.args.get("success") # Hämta success från URL:en
    return render_template("index.html", success = success) # Skicka success till index.html       

@app.route("/add", methods=["POST"]) # Endast POST-metoden tillåten
def add():
    service = request.form.get("service") # Hämta service från formuläret
    password = request.form.get("password") # Hämta password från formuläret
    
    hashed_password = generate_password_hash(password) # Kryptera lösenordet
    new_account = Account(service=service, password=hashed_password) # Skapa nytt Account-objekt
    db.session.add(new_account) # Lägg till i databasen
    db.session.commit() # Spara i databasen
    flash("Registration successfull! Try logging in.") 
    return redirect(url_for("home", success="true")) 
    

@app.route("/get", methods=["POST"])
def get_password():
    service = request.form.get("service") # Hämta service från formuläret
    user = Account.query.filter_by(service=service).first() # Hämta användaren från databasen
    
    if user: # Om användaren finns
        flash(f"The password for {service} is {user.password}") # Skicka lösenordet
        return redirect(url_for("home", success="true")) # Skicka till index.html med success
    else:
        flash(f"No password stored for {service}, try another one.") # Annars skicka felmeddelande
        return redirect(url_for("home")) 

