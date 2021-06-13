# caeserCipher.py
# Encrypts text using a simple caeser cipher.
# A caeser cipher takes an alphabetical letter,
# and encrypts it by changing the letter to another
# 'x' characters away. For example, the letter B is
# the 2nd letter of the alphabet. With a caeser
# cipher using a key of 3, B would become E (letter 5)

# Imports
import os
import time

# Functions
def show_caeser_title():
    os.system('cls')
    print("******************************************************")
    print("*****          AIOCrypt - Caeser cipher          *****")
    print("******************************************************")
    print("\nThis script encrypts text using a simple Caeser cipher.\n")

def get_user_input():
    print("[1] Encrypt text")
    print("[2] How it works")
    print("\n[q] Return to previous menu")
    return input("\nMake a selection: ")

def selectKey():
    key = ''
    validKey = False

    os.system('cls')
    print('Enter a number between 1 and 25 to act as a key')

    while validKey == False:
        try:
            key = int(input("Key: "))
            assert 1 <= key <= 25
        except:
            print("\nPlease enter a whole number between 1 and 25")
        else:
            validKey == True
            return key

def explainCipher():
    os.system('cls')
    print("explainCipher")
    os.system('pause')
    return

def encryptText(textToEncrypt, key):
    os.system('cls')
    print("Encrypting your text...")
    # TODO - Add encryption routine
    time.sleep(3)
    os.system('cls')
    print("Completed! Your text has been encrypted using a key of " + str(key) + ".")
    print("\nOriginal text: " + textToEncrypt)
    print("\nNew text: " + "ENCRYPTED_TEXT" + "\n")
    # TODO - Print text
    # TODO - Print to text file
    os.system('pause')


# Main
def main(textToEncrypt):
    userInput = ''
    key = ''

    while userInput != 'q':
        show_caeser_title()
        userInput = get_user_input()

        if userInput == '1':
            key = selectKey()
            print(key)
            encryptText(textToEncrypt, key)
        
        elif userInput == '2':
            explainCipher()
        elif userInput == 'q':
            break