#pPassword generator in Python

import random 
import string

#defining a function to generate a random password
def generate_password(length = 12):
    
    #defining characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    #generating random password fron the defined set (characters)
    password = ' '.join(random.choice(characters) for i in range(length))
    
    return password

#getting the desired length of the password from the user
password_length = int(input("Enter the length of the password: "))

#generate the password
pass_word = generate_password(password_length)

#print the generated password
print("Generated password: ",pass_word)