from app import create_app # Importera create_app från app/__init__.py

app = create_app()  # Skapa appen

if __name__ == "__main__":
    app.run(debug=True)  # Kör appen