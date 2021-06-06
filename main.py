# main.py
# Handles user input and selection, then passes the user
# choice to the relevent encryption / decryption tools

# Imports
import os
import textEncryption
import fileEncryption
import textDecryption
import fileDecryption

# Functions
def show_title_bar():
    os.system('cls')

    print("******************************************************")
    print("*****                  AIOCrypt                  *****")
    print("******************************************************")
    print("\nWelcome to AIOCrypt. This software is designed to enable")
    print("you to easilly encrypt and decrypt text file and various")
    print("other file types using a variety of encryption methods\n")

def get_user_input():
    os.system('cls')
    print("[1] Encrypt some text")
    print("[2] Encrypt a file")
    print("\n[3] Decypt some text")
    print("[4] Decypt a file")
    print("\n[q] Quit")

    return input("\nMake a selection: ")

def text_encryption():
    os.system('cls')
    print("Text encryption selected\n")
    textEncryption.main()

def file_encryption():
    os.system('cls')
    print("File encryption selected\n")
    fileEncryption.main()

def text_decryption():
    os.system('cls')
    print("Text decryption selected\n")
    textDecryption.main()

def file_decryption():
    os.system('cls')
    print("File decryption selected\n")
    fileDecryption.main()

def main():
    user_input = ''
    show_title_bar()
    os.system('pause')

    # Loop through the user options
    while user_input != 'q':
        user_input = get_user_input()

        # Display the user's choice
        if user_input == '1':
            text_encryption()
            break
        elif user_input == '2':
            file_encryption()
            break
        elif user_input == '3':
            text_decryption()
            break
        elif user_input == '4':
            file_decryption()
            break

# Initialisation
if __name__ == '__main__':
    main()
