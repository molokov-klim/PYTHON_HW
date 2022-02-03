

def read_one(email, user_storage, email_have):
    print("read one")
    for key in user_storage:
        if email == key:
            print(email, user_storage[key])
            email_have = True
    if not email_have:
        print("Email не найден")
    email_have = False

def read_all(user_storage):
    for key in user_storage:
        print(key, user_storage[key])
