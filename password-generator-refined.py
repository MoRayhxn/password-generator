import random
print("".join(random.choice([chr(x) for x in range(32,127)])for x in range (int(input("Enter the desired length of your password: ")))))

# chr are all characters - range 32,127 are all variations of the ASCII table (printable characters)
# uses for loop to repeat the random character joining for the the desired length which is "x"