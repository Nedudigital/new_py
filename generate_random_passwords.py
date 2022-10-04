import random
import string
#first import random and string modules
#next define a function for the length of the password
#make the letters equal to the ask
def get_password(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("Random string of length", length, "is:", result_str)
