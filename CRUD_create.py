

def create_user(email, name, password, phone, user_emails, user_storage):
    print("start create")
    user_info = [email, name, password, phone]
    user_emails.append(email)
    user_storage[email]={
        "name":name,
        "password":password,
        "phone":phone
    }

    print("Добавлен пользователь: ", user_info)
    return None

