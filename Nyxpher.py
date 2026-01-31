import time
import os

# -----------------------------
# Utilities
# -----------------------------
def clear():
    os.system("cls" if os.name == "nt" else "clear")


# -----------------------------
# ANSI Colors
# -----------------------------
RESET   = "\033[0m"
RED     = "\033[31m"
GREEN   = "\033[32m"
YELLOW  = "\033[33m"
BLUE    = "\033[34m"
MAGENTA = "\033[35m"
CYAN    = "\033[36m"
WHITE   = "\033[37m"
BOLD    = "\033[1m"


# -----------------------------
# Banner & Intro
# -----------------------------
def show_banner():
    print(WHITE + "                              Developed by" + RESET)
    print(RED + r"""
▄█    ▄▄▄▄▀ ▄▄▄▄▄   █▀▄▀█ ██     ▄▄▄▄▀ ▄▄▄▄▀ ▄▄▄▄▄      ▄▄▄▄▀ ▄  █ ▄███▄     ▄ ▄   ████▄ █    ▄████  
██ ▀▀▀ █   █     ▀▄ █ █ █ █ █ ▀▀▀ █ ▀▀▀ █   █     ▀▄ ▀▀▀ █   █   █ █▀   ▀   █   █  █   █ █    █▀   ▀ 
██     █ ▄  ▀▀▀▀▄   █ ▄ █ █▄▄█    █     █ ▄  ▀▀▀▀▄       █   ██▀▀█ ██▄▄    █ ▄   █ █   █ █    █▀▀    
▐█    █   ▀▄▄▄▄▀    █   █ █  █   █     █   ▀▄▄▄▄▀       █    █   █ █▄   ▄▀ █  █  █ ▀████ ███▄ █      
 ▐   ▀                 █     █  ▀     ▀                ▀        █  ▀███▀    █ █ █            ▀ █     
                      ▀     █                                  ▀             ▀ ▀                ▀    
                           ▀                                                                         
""" + RESET)
    time.sleep(3)
    print("Starting program...")
    print("Please, wait...")
    time.sleep(3)
    print(CYAN + r"""
M"'"'"'"`YM                            dP                                     d88  
M  mmmm.  M                            88                                      88  
M  MMMMM  M dP    dP dP.  .dP 88d888b. 88d888b. .d8888b. 88d888b.    dP   .dP  88  
M  MMMMM  M 88    88  `8bd8'  88'  `88 88'  `88 88ooood8 88'  `88    88   d8'  88  
M  MMMMM  M 88.  .88  .d88b.  88.  .88 88    88 88.  ... 88          88 .88'   88  
M  MMMMM  M `8888P88 dP'  `dP 88Y888P' dP    dP `88888P' dP          8888P'   d88P 
MMMMMMMMMMM      .88          88                                                   
             d8888P           dP                                                   

                              NYXPHER — powered by Nyx27
""" + RESET)


def show_repo():
    print(YELLOW + "Official repository:" + RESET)
    print(RED + "https://github.com/ItsMattsTheWolf/Nyxpher" + RESET)


# -----------------------------
# Nyx27 Cipher
# -----------------------------
ALPHABET = [
    "a","b","c","d","e","f","g","h","i","j","k","l","m",
    "n",
    "ñ","o","p","q","r","s","t","u","v","w","x","y","z"
]

INDEX = {char: i for i, char in enumerate(ALPHABET)}


def nyx27_transform(text):
    result = ""

    for char in text:
        lower = char.lower()

        if lower in INDEX:
            idx = INDEX[lower]
            mirror_idx = 26 - idx
            new_char = ALPHABET[mirror_idx]

            # Preserve original case
            if char.isupper():
                new_char = new_char.upper()

            result += new_char
        else:
            # Non-alphabet characters stay the same
            result += char

    return result


# -----------------------------
# Main Menu
# -----------------------------
def main_menu():
    while True:
        print(GREEN + "\n1) Encrypt" + RESET)
        print(GREEN + "2) Decrypt" + RESET)
        print(GREEN + "3) Exit" + RESET)

        choice = input("> Please, choose one: ")

        if choice == "1":
            text = input("> Enter text to encrypt: ")
            print(MAGENTA + "\nEncrypted text:" + RESET)
            print(WHITE + nyx27_transform(text) + RESET)

        elif choice == "2":
            text = input("> Enter text to decrypt: ")
            print(MAGENTA + "\nDecrypted text:" + RESET)
            print(WHITE + nyx27_transform(text) + RESET)

        elif choice == "3":
            print(YELLOW + "Exiting Nyxpher..." + RESET)
            break

        else:
            print(RED + "Invalid option." + RESET)


# -----------------------------
# Entry Point
# -----------------------------
def main():
    clear()
    show_banner()
    time.sleep(2)

    show_repo()
    time.sleep(2)

    main_menu()


if __name__ == "__main__":
    main()
