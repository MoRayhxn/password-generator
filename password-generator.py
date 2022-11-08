import random

print("Let's generate your new password!")

### Define characters
characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz1@#£$%^&*()"

### Ask user for desired password length
### Two options, can ask a user how many characters they want, or make it completely random.
# passwordLength = int(input("How long would you like you password to be? "))

passwordLength = random.randint(0, 20)

### Generate password
newPassword = []
for x in range(passwordLength):
    ### add (append) a ramdp, cjaracter to password
    newPassword.append(random.choice(characters))

### Join everyhing back into a string
finalPassword = ''.join(map(str, newPassword))

### Display new password
print("\nYour new password is:", finalPassword)
