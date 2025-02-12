import random  # A library that contains functions for generating random numbers
import string  # A library that contains ASCII characters
import os  # A library that contains functions for interacting with the operating system

KEY_FILE = "key.txt"  # Filnamn för att spara krypteringsnyckeln

# Skapar en sträng med alla ASCII-tecken och mellanslag
chars = " " + string.punctuation + string.ascii_letters + string.digits + "åäöÅÄÖ" 
chars = list(chars) # Gör om strängen till en lista 

# Generera eller läs krypteringsnyckeln
def load_key():
    if os.path.exists(KEY_FILE): # Om filen finns
        with open(KEY_FILE, "r") as file: # Öppna filen för att läsa
            key = file.read() # Läser innehållet i filen
    else: # Om filen inte finns 
        key = chars.copy() # Kopiera listan till key 
        random.shuffle(key)
        with open(KEY_FILE, "w") as file: 
            file.write("".join(key)) # Skriv nyckeln till filenyckeln
    return key

key = load_key() # Laddar krypteringsnyckeln från filenyckeln


# Kryptera lösenord
def encrypt(text):
    encrypted_text = ""  # Tom sträng för att lagra det krypterade lösenordet
    for char in text: # Loopar igenom varje tecken i texten aka lösenordet
        index = chars.index(char) # Hämtar index för tecknet
        encrypted_text += key[index] # Lägger till det krypterade tecknet
    return encrypted_text # Returnerar det krypterade lösenordet

def decrypt(text):
    decrypted_text = ""  
    for char in text: # Loopar igenom varje tecken i texten aka lösenordet
        index = key.index(char) # Hämtar index för tecknet
        decrypted_text += chars[index] # Lägger till det dekrypterade tecknet
    return decrypted_text # Returnerar det dekrypterade lösenordet