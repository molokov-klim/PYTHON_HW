import os
import shutil
from CRUD_create import create_user
from CRUD_read import read_one, read_all
from CRUD_update import update
from CRUD_delete import delete

user_emails=[]
user_storage={}


def menu():
    help =('exit = close program; 1 = create user; 2 = read; 3 = update; 4 = delete; help = help')
    print(help)
    cmd = input("Вы в главном меню. Введите команду: ")
    while cmd != "exit":
        if cmd == "1":
            print("Выбрана 1 = create user. Введите данные нового пользователя")
            email = input("Email: ")
            name = input("Name: ")
            password = input("Password: ")
            phone = input("Phone: ")
            create_user(email, name, password, phone, user_emails, user_storage)
            print("user_emails =", user_emails)
            print("user_storage =", user_storage)
        elif cmd == "2":
            help2 = ("1 = read all users; 2 = read one user; 0 = return to main menu")
            print(help2)
            cmd2 = input("Вы в меню вывода пользователей. Введите команду ")
            while cmd2 != "0":
                if cmd2 == "1":
                    print("Выбрана 1 = read all users")
                    read_one()
                elif cmd2 == "2":
                    print("Выбрана 2 = read one user. Введите идендификатор пользователя")
                    read_all()
                elif cmd2 == "help":
                    print(help2)
                else:
                    print("Такой команды нет!")
                cmd2 = input("Вы в меню вывода пользователей. Введите команду ")
        elif cmd == "3":
            update()
        elif cmd == "4":
            delete()
        elif cmd == "help":
            print(help)
        elif cmd == "test":
            print("test")
        else:
            print("Такой команды нет!")
        cmd = input("Вы в главном меню. Введите команду: ")
    return

if __name__ == "__main__":
  menu()










