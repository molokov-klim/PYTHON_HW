import os
import shutil
from CRUD_create import create
from CRUD_read import read
from CRUD_update import update
from CRUD_delete import delete

users={
    "1":{"email": "some@email.com",
        "name": "Some Name",
        "phone": "9090909090"}
}


def menu():
    help =('exit = close program; 1 = create; 2 = read; 3 = update; 4 = delete')
    print(help)
    cmd = input("Введите команду: ")
    while cmd != "exit":
        if cmd == "1":
            create()
        elif cmd == "2":
            read()
        elif cmd == "3":
            update()
        elif cmd == "4":
            delete()
        elif cmd == "help":
            print(help)
        elif cmd == "test":
            for i in range(len(users)):
                print("userID: ", users.i)
        else:
            print("Такой команды нет!")
        cmd = input("Введите команду: ")
    return

if __name__ == "__main__":
  menu()










