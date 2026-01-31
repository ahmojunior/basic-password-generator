import string
import random
import time

# Variables ========
alphabet = string.ascii_letters
digits = string.digits
punctuation = string.punctuation
characters = list(alphabet + digits + punctuation)

# Our "Password Generator" ========
def generatePassword(length):
    # I will use "while", since i am more used to it.
    password = ""
    i = 0
    while i < int(length):
        password = password + str(characters[random.randrange(0, len(characters))])
        i += 1    
    return password


# some bs, but it looks cool.
def main():
    print("Welcome to the Password Generator!")
    while True:
        leng = input("How long your password will be? : ")
        try:
            n = int(leng)
            if n <= 0:
                print("Please enter a positive integer greater than zero.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer (e.g. 12).")
    print("\nCreating your password...\n")
    time.sleep(4)
    print(generatePassword(leng))

if __name__ == "__main__":
    main()
