from flask import redirect, url_for, render_template, request, flash
from werkzeug.security import generate_password_hash 
from app.models import db, Account # Importera db och Account från models.py
from flask import current_app as app # Importera app från __init__.py
from app.encrypt import encrypt, decrypt # Importera encrypt och decrypt från encrypt.py
from app.reminder import reminder # Importera reminder från timer.py
from datetime import datetime, timedelta # Importera datetime för att räkna dagar
import threading # Importera threading för att köra funktioner i bakgrunden

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

    new_account = Account(service=service, hashed_password=hashed_password, encrypted_password=encrypted_password, created_at=datetime.now()) # Skapa nytt Account-objekt
    db.session.add(new_account) # Lägg till i databasen
    db.session.commit() # Spara i databasen
    flash("Registration successfull! Try logging in.") 


    threading.Thread(target=reminder, args=(service,)).start() # Starta en ny tråd för att köra reminder-funktionen för lösenordet
    reminder(service) # Starta reminder-funktionen i bakgrunden

    return redirect(url_for("home", success="true")) 
    

@app.route("/get", methods=["POST"])
def get_password():
    service = request.form.get("service") # Hämtar service från formuläret
    account = Account.query.filter_by(service=service).first() # Hämtar användaren från databasen
    
    if account: # Om användaren finns
        decrypted_password = decrypt(account.encrypted_password) # Dekryptera lösenordet
        flash(f"The password for {service} is {decrypted_password}") # Skicka lösenordet
        return redirect(url_for("home"))
    else:
        flash(f"No password stored for {service}, try another one.") # Annars skicka felmeddelande
        return redirect(url_for("home")) 

@app.route("/reminders", methods=["POST"])
def reminders():
    threshold_time = datetime.now() - timedelta(seconds=10) # Tiden som används för att filtrera konton som har gått ut
    old_accounts = Account.query.filter(Account.created_at < threshold_time).all() # Hämta alla konton som är äldre än 10 sekunder
    return render_template("index.html", old_accounts=old_accounts) # Skicka med old_accounts till home