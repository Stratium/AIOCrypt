# textEncryption.py
# Asks user to select a method of text encryption
# and gets text input, then passes it to correct
# encryption script

# Imports
import os
from TextEncryption import caeserCipher

# Functions
def show_text_title():
    os.system('cls')
    print("******************************************************")
    print("*****         AIOCrypt - Text Encryption         *****")
    print("******************************************************")
    print("\nThis script allows you to encrypt a text string using a")
    print("variety of different encryption methods.\n")

def get_text_to_encrypt():
    print("Please enter the text string you wish to encrypt.")
    print("Both alphanumeric characters and symbols are permitted.")

    return input("\nEnter text: ")

def get_user_confirmation(textToEncrypt):
    os.system('cls')
    print("You have entered the following string:")
    print("\n" + textToEncrypt)
    return input("\nIs this correct? [y/n]: ")

def get_cipher_selection():
    os.system('cls')
    print("Select encryption method:")
    print("\n[1] Caeser Cipher")
    print("\n[q] Return to previous menu")

    return input("\nMake a selection: ")


# Main
def main():
    userSelection = ''
    textToEncrypt = ''
    confirmText = 'n'
    doLoop = True

    show_text_title()

    while confirmText != 'y':
        if confirmText == 'n':
            textToEncrypt = get_text_to_encrypt()
            os.system('cls')
            confirmText = get_user_confirmation(textToEncrypt)
            os.system('cls')
        else:
            confirmText = get_user_confirmation(textToEncrypt)
            os.system('cls')

    while doLoop == True:
        userSelection = get_cipher_selection()

        # Pass user choice to correct script
        if userSelection == '1':
            caeserCipher.main(textToEncrypt)
        elif userSelection == 'q':
            break              
