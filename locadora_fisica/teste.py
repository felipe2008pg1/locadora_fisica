from datetime import datetime
import time
import os
import random

data = [{'user': 'felipe2008pg1', 'password': '123'},
        {'user': 'felipe', 'password': '123'},
        {'user': 'carlos3123', 'password': '13453'},
        {'user': 'nitay234', 'password': '123'},
        {'user': 'falcaocorrea', 'password': '123'}]

def super_crypt(password, username):
    seed_value = sum(ord(c) for c in password) + sum(ord(c) for c in username)
    random.seed(seed_value) 
    chars = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    crypto_string = "".join(random.choice(chars) for _ in range(32))
    return crypto_string

def low_write(word):
    for lyric in word:
        print(lyric, end='', flush=True)
        time.sleep(0.03)
    print() 

def show_datetime():
    br = datetime.now()
    return br.strftime("%d/%m/%Y - %H:%M:%S")

def screen_clean():
    os.system("cls" if os.name == "nt" else "clear")

while True:
    screen_clean()
    low_write("\nWELCOME TO MY LOGIN SYSTEM (At the moment, it is only in English).")
    try:
        choice = int(input(
            "\n1 - Login \n2 - Register \n3 - Show the Datetime \n4 - Left \n5 - See the database (ONLY TESTS) \n -- CHOOSE A VALID NUMBER: "))
        if choice == 1:
            login_user = input("Type your user: ").strip()
            login_password = input("Type your password: ").strip()
            found = False

            for search in data:
                if search['user'] == login_user and search['password'] == login_password:
                    found = True
                    low_write("Login sucessfuly")
                    time.sleep(1)

        elif choice == 2:
            register_user = input("Type your new user: ").strip()
            found = False

            for search in data:
                if search['user'] == register_user:
                    found = True
                    break

            if found:
                low_write("This user already exists, try another.")
                time.sleep(1)
            else:
                register_password = input("Type your new password: ").strip()
                data.append({'user': register_user,'password': register_password})
                low_write("Register done! Come to home and try the login.")
                time.sleep(1)

        elif choice == 3:
            print(show_datetime())
            input("Press ENTER for back on home.")

        elif choice == 4:
            print("="*10)
            low_write("Shutting down...")
            print("="*10)
            break

        elif choice == 5:
            print("\n--- DATABASE ---")
            for i, t in enumerate(data, start=1):
                encrypted_password = super_crypt(t['password'], t['user'])
                print(f"{i} - User: {t['user']:<15} | Password (Encrypted): {encrypted_password}")
            input("\nPress ENTER to go back home.")

        else:
            low_write("Sorry, your index not is valid, try again.")
            time.sleep(1)

    except ValueError:
        low_write("[ERRO] Just type a valid option.")
        time.sleep(1)
