# Password strength checking
jest = input("\nEnter the password: ")

uppercase = False
lowercase = False
digit = False
specialchar = False

special = "!@#$%^&*()-_=+[]{}|\\';,./:~<>"

length = False
if len(jest) >= 8:
    length = True

for char in jest:
    if 'A' <= char <= 'Z':
        uppercase = True
    if 'a' <= char <= 'z':
        lowercase = True
    if '0' <= char <= '9':
        digit = True
    if char in special:
        specialchar = True

criteria = 0

if length:
    criteria += 1
if uppercase:
    criteria += 1
if lowercase:
    criteria += 1
if digit:
    criteria += 1
if specialchar:
    criteria += 1

if criteria == 5:
    print("Password strength: STRONG!")
elif criteria >= 3:
    print("Password strength: MODERATE")
else:
    print("Password strength: WEAK")
