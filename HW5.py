import os
from tkinter import filedialog
import shutil
import sys
from CRUD_create import create_user
from CRUD_read import read_one, read_all
from CRUD_update import update
from CRUD_delete import delete
from User_generator import generate
from test import test
import json
import jsonschema
from jsonschema import validate

schema = {
    "title": "email",
    "description": "email",
    "type": "object",
    "properties":   {
            "name":         {
            "description": "name",
            "type": "string"
                            },
            "password":     {
            "description": "password",
            "type": "string"
                            },
            "phone":        {
            "description": "phone",
            "type": "string"
                            },
            "required": ["name", "password", "phone"]
                    },
    "required": ["email"]
}

#     "productName": {
#       "description": "Name of the product",
#       "type": "string"
#     },
#     "price": {
#       "description": "The price of the product",
#       "type": "number",
#       "exclusiveMinimum": 0
#     },
#     "tags": {
#       "description": "Tags for the product",
#       "type": "array",
#       "items": {
#         "type": "string"
#       },
#       "minItems": 1,
#       "uniqueItems": true
#     }
#   },
#   "required": [ "productId", "productName", "price" ]
# }

user_emails = []
user_storage = {}
email_have = False
filename = ""
user_qty = 0

def menu():
    global email_have
    help =('exit = close program; 1 = create user; 2 = read user; 3 = update user; 4 = delete user; 5 = file; 6 = generate users; help = help')
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
            print("Выбрана 4 = delete user. Введите данные пользователя: ")
            email = input("Email: ")
            delete(email, user_storage, user_emails, email_have)
        elif cmd == "help":
            print(help)
        elif cmd == "test":
            test()
        elif cmd == "5":
            print("Выбрана 5 = file")
            help3 = ("1 = create file; 2 = read file; 3 = update file; 4 = delete file; 5 = show files; 0 = return to main menu; help = help")
            print(help3)
            cmd3 = input("Вы в меню работы с файлами. Введите команду: ")
            while cmd3 != "0":
                if cmd3 == "1":
                    print("Выбрана 1 = create file. Введите название файла: ")
                    print('Укажите директорию')
                    directory = filedialog.askdirectory()
                    filename = input('Введите имя файла: ')
                    extension = input('Введите расширение: ')
                    try:
                        with open(directory + '/' + filename + '.' + extension, 'w') as tw:
                            tw.write('')
                            print("Файл создан: ", filename+"."+extension)
                    except:
                        print('Что-то пошло не так')

                elif cmd3 == "2":
                    print("Выбрана 2 = read file")
                    print('Выберите файл')
                    file_path = filedialog.askopenfilename()
                    print(file_path)
                    with open('out.txt', 'r', -1, 'utf-8') as inp:
                        for i in inp.readlines():
                            key, val = i.strip().split(':')
                            user_storage[key] = val

                elif cmd3 == "3":
                    print("Выбрана 3 = update file")
                    print('Выберите файл')
                    file_path = filedialog.askopenfilename()
                    print(file_path)
                    with open(file_path, 'w', -1, 'utf-8') as out:
                        for key, val in user_storage.items():
                            out.write('{}:{}\n'.format(key, val))

                elif cmd3 == "4":
                    print("Выбрана 4 = delete file")

                elif cmd3 == "5":
                    print("Выбрана 5 = show files")
                    path = '.'
                    rez = sorted(os.listdir(path))
                    for n, item in enumerate(rez):
                        print(n + 1, item)

                elif cmd3 == "help":
                    print(help3)
                elif cmd3 == "exit":
                    sys.exit()
                else:
                    print("Введенной команды не существует")
                    print(help3)
                cmd3 = input("Вы в меню работы с файлами. Введите команду: ")

        elif cmd == "6":
            print("Выбрана 6 = generate users. Операция перезапишет текущие данные. Для отмены операции оставьте поле ввода количества пустым")
            user_qty = input("Введите количество пользователей для генерации: ")
            if user_qty != "" and user_qty != 0:
                generate(user_qty, user_emails, user_storage)

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





