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

# Main
def main():
    user_input = ''
    show_title_bar()
    os.system('pause')

    # Loop through console UI
    while user_input != 'q':
        user_input = get_user_input()

        # Pass user choice to correct script
        if user_input == '1':
            textEncryption.main()
            break
        elif user_input == '2':
            fileEncryption.main()
            break
        elif user_input == '3':
            textDecryption.main()
            break
        elif user_input == '4':
            fileDecryption.main()
            break

# Initialisation
if __name__ == '__main__':
    main()
