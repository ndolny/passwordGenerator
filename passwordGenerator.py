import random
import string


letters = string.ascii_letters
numbers = string.digits
scharacters = string.punctuation
password = "".join(random.choice(letters+numbers+scharacters) for i in range (15))
 
print("Your new password: " + password) 