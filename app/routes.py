from flask import redirect, url_for, render_template, request, flash
from werkzeug.security import check_password_hash, generate_password_hash 
from app.models import db, Account # Importera db och Account från models.py
from flask import current_app as app # Importera app från __init__.py
from app.encrypt import encrypt, decrypt # Importera encrypt och decrypt från encrypt.py

@app.route("/")
def home():
    success = request.args.get("success") # Kollar omm success finns i URL:en, för att visa pop-up meddelande
    return render_template("index.html", success = success) # Laddar sidan och skickar med 'success' för att visa pop-up om det behövs 

@app.route("/add", methods=["POST"]) # Endast POST-metoden tillåten
def add():
    service = request.form.get("service") # Hämtar service från formuläret
    password = request.form.get("password") # Hämtar password från formuläret

    encrypted_password = encrypt(password) # Krypterar lösenordet
    hashed_password = generate_password_hash(password) # Hashar lösenordet

    new_account = Account(service=service, hashed_password=hashed_password, encrypted_password=encrypted_password) # Skapa nytt Account-objekt
    db.session.add(new_account) # Lägg till i databasen
    db.session.commit() # Spara i databasen
    flash("Registration successfull! Try logging in.") 
    return redirect(url_for("home", success="true")) 
    

@app.route("/get", methods=["POST"])
def get_password():
    service = request.form.get("service") # Hämtar service från formuläret
    account = Account.query.filter_by(service=service).first() # Hämtar användaren från databasen
    
    if account: # Om användaren finns
        decrypted_password = decrypt(account.encrypted_password) # Dekryptera lösenordet
        flash(f"The password for {service} is {decrypted_password}") # Skicka lösenordet
        return redirect(url_for("home", success="true")) # Skicka till index.html med success
    else:
        flash(f"No password stored for {service}, try another one.") # Annars skicka felmeddelande
        return redirect(url_for("home")) 

