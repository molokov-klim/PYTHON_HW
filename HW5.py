import os
import shutil
import sys
from CRUD_create import create_user
from CRUD_read import read_one, read_all
from CRUD_update import update
from CRUD_delete import delete
from test import test

user_emails = []
user_storage = {}
email_have = False

def menu():
    global email_have
    help =('exit = close program; 1 = create user; 2 = read user; 3 = update user; 4 = delete user; help = help')
    print(help)
    cmd = input("Вы в главном меню. Введите команду: ")
    while cmd != "exit":
        if cmd == "1":
            print("Выбрана 1 = create user. Введите данные нового пользователя")
            email = input("Email: ")
            name = input("Name: ")
            password = input("Password: ")
            phone = input("Phone: ")
            for i in user_emails:
                if email == i:
                    print("Такой email уже существует. Пожалуйста используйте другой")
                    email_have = True

            if not email_have:
                create_user(email, name, password, phone, user_emails, user_storage)
                print("user_emails =", user_emails)
                print("user_storage =", user_storage)

            email_have = False

        elif cmd == "2":
            print("Выбрана 2 = create user")
            help2 = ("1 = read one users; 2 = read all user; 0 = return to main menu; help = help")
            print(help2)
            cmd2 = input("Вы в меню вывода пользователей. Введите команду: ")
            while cmd2 != "0":
                if cmd2 == "1":
                    print("Выбрана 1 = read one user. Введите email пользователя: ")
                    email = input("Email: ")
                    read_one(email, user_storage, email_have)
                elif cmd2 == "2":
                    print("Выбрана 2 = read all users")
                    read_all(user_storage)
                elif cmd2 == "help":
                    print(help2)
                elif cmd2 == "exit":
                    sys.exit()
                else:
                    print("Введенной команды не существует")
                    print(help2)
                cmd2 = input("Вы в меню вывода пользователей. Введите команду ")
        elif cmd == "3":
            print("Выбрана 3 = update user. Введите данные пользователя")
            email = input("Email: ")
            update(email, user_emails, user_storage, email_have)
            print("user_emails: ", user_emails)
            print("user_storage: ", user_storage)
        elif cmd == "4":
            delete()
        elif cmd == "help":
            print(help)
        elif cmd == "test":
            test()
        elif cmd == "":
            print("Введенной команды не существует")
            print(help)
        else:
            print("Введенной команды не существует")
            print(help)
        cmd = input("Вы в главном меню. Введите команду: ")
    return

if __name__ == "__main__":
  menu()





