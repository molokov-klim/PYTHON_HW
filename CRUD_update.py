

def update(email, user_emails, user_storage, email_have):
    print("start update")
    old_email = email
    new_email_have = False
    new_email = email

    for key in user_storage:
        if email == key:
            print(email, user_storage[key])
            email_have = True
    if email_have:
        new_email = input("Введите новый email (оставьте пустым чтобы не вносить изменений): ")

        for i in user_emails:
            if new_email == i:
                print("Такой email уже существует. Пожалуйста используйте другой")
                new_email_have = True

        if not new_email_have:
            if new_email != "":
                for key, email in enumerate(user_emails):
                    # print("key: ", key)
                    # print("email: ", email)
                    # print("user_emails[key]: ", user_emails[key])
                    if user_emails[key] == old_email:
                        user_emails[key] = new_email
                user_storage[new_email] = user_storage.pop(old_email)

            if new_email == "":
                new_email = old_email

        new_email_have = False

    if not email_have:
        print("Email не найден")
    email_have = False

    for key in user_storage:
        if email == key:
            email_have = True
        if new_email == key:
            email_have = True
    if email_have:
        new_name = input("Введите новый name (оставьте пустым чтобы не вносить изменений): ")
        if new_name != "":
            user_storage[new_email]["name"] = new_name

        new_password = input("Введите новый password (оставьте пустым чтобы не вносить изменений): ")
        if new_password != "":
            user_storage[new_email]["password"] = new_password

        new_phone = input("Введите новый phone (оставьте пустым чтобы не вносить изменений): ")
        if new_phone != "":
            user_storage[new_email]["phone"] = new_phone

    return None