import random  # A library that contains functions for generating random numbers
import string  # A library that contains ASCII characters

chars = " " + string.punctuation + string.digits + string.ascii_letters + "åäöÅÄÖ" # One string that contains all ASCII characters
chars = list(chars) # Convert the string to a list
key = chars.copy() # Copy the list

random.shuffle(key) # Shuffle the key



#Encrypt function
def encrypt(text):  
    encrypted = "" # An empty string to store the encrypted text    
    for char in text:       
        index = chars.index(char) # Find the index of the character in the chars list  
        encrypted += key[index] # Add the character at the same index in the key list to the encrypted string
    return encrypted # Return the encrypted string to (text)

#Decrypt function
def decrypt(text):
    decrypted = "" # An empty string to store the decrypted text
    for char in text:
        index = key.index(char) # Find the index of the character in the key list
        decrypted += chars[index] # Add the character at the same index in the chars list to the decrypted string
    return decrypted # Return the decrypted string to (text)

