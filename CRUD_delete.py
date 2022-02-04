
def delete(email, user_storage, user_emails, email_have):
    print("start delete")
    email_have = False
    for i in user_emails:
        if email == i:
            try:
                if email != "":
                    del user_storage[email]
                    user_emails.remove(email)
            finally:
                if email != "":
                    print("Пользователь удален")
                    print("user_emails: ", user_emails)
                    print("user_storage: ", user_storage)
            email_have = True
    if not email_have:
        print("Пользователь не найден")

    return None