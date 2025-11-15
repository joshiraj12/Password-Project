import random

# Character lists
a = []
for q in range(65, 91):
    a.append(q)

smallalp = []
for j in range(97, 123):
    smallalp.append(j)

spesala = []
for w in range(33, 48):
    spesala.append(w)

numb = []
for v in range(48, 58):
    numb.append(v)

# Password length choices
n = [8, 9, 10, 11, 12, 13, 14, 15, 16]
c = random.choice(n)

# Generate password
passW = []
for i in range(c):
    b = random.choice(a)
    d = random.choice(smallalp)
    e = random.choice(spesala)
    f = random.choice(numb)

    u = chr(b)
    x = chr(d)
    y = chr(e)
    z = chr(f)

    met = [u, x, y, z]
    dem = random.choice(met)

    passW.append(dem)

jest = ''.join(passW)
print("\nThe generated password:", jest)

import datetime
import os

# Save password
ch = input("Do you want to save this password? (yes/no): ")

if ch == 'yes':
    # File name
    filename = "saved_passwords.txt"

    # Check existing count
    if os.path.exists(filename):
        with open(filename, "r") as f:
            lines = f.readlines()
            serial = len(lines) + 1
    else:
        serial = 1

    # Current date and time
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Save entry
    with open(filename, "a") as file:
        file.write(f"{serial}. Password: {jest} | Saved on: {now}\n")

    print("The password has been saved in saved_passwords.txt")

if ch == 'no':
    print("THANKS FOR USING THE PROGRAM")