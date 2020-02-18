import random
import string

def randomStringDigits(stringLength):
        """Generate a random string of letters and digits """

        password_characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice( password_characters) for i in range(stringLength))

print ("Generating a Random String including letters and digits")
print ("First Random String is  ", randomStringDigits(12))
print ("Second Random String is ", randomStringDigits(12))
print ("Third Random String is  ", randomStringDigits(12))
print ("Fourth Random String is  ", randomStringDigits(12))
