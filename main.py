import string
import secrets
import pyperclip

def genPass(Length=12):
    passChars = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.digits),
        secrets.choice(string.punctuation)
    ]
    allBucket = ( string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation )
    for _ in range(Length - 4):
        passChars.append(secrets.choice(allBucket))
    secrets.SystemRandom().shuffle(passChars)
    return "".join(passChars)
Len = int(input("Please enter the desires Password length: "))
Password = genPass(Length=Len)
print(Password)
pyperclip.copy(Password)
print("Password Copied to Clipboard !")
