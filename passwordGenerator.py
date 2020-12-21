import random
import string


letters = string.ascii_letters
numbers = string.digits
scharacters = string.punctuation

passwordLength = input("Length of required password: ")
password = "".join(random.choice(letters+numbers+scharacters) for i in range (passwordLength))
 
print("Your new password: " + password) 
