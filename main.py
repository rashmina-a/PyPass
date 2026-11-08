import string
import secrets
import pyperclip
def askOptions():
    symbols = input("Do you want to Include Symbols ( Y/N ) :  ").lower()
    digits = input("Do you want to Include Numbers ( Y/N ) :  ").lower()
    return symbols,digits
def genPass(Length=12):
    passChars = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase)
    ]
    allBucket = ( string.ascii_lowercase + string.ascii_uppercase )
    symbols,digits = askOptions()
    if symbols == "y":
        passChars.append(secrets.choice(string.punctuation))
        allBucket += string.punctuation
    if digits == "y":
        passChars.append(secrets.choice(string.digits))
        allBucket += string.digits
    for _ in range(Length - 4):
        passChars.append(secrets.choice(allBucket))
    secrets.SystemRandom().shuffle(passChars)
    return "".join(passChars)
Len = int(input("Please enter the desired Password length: "))
Password = genPass(Length=Len)
print(Password)
pyperclip.copy(Password)
print("Password Copied to Clipboard !")