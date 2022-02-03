import requests

def generate(user_qty, user_emails, user_storage):

    basic_url = 'http://api.randomuser.me/?results='
    url = basic_url+user_qty
    print("GET ", url)

    res = requests.request("GET", url)
    res = res.json()
    #print(res["results"])

    for user in res["results"]:
        user_emails.append(user["email"])
        user_storage[user["email"]] = {
            "name": user["name"]["first"]+" "+user["name"]["last"],
            "password": user["login"]["password"],
            "phone": user["phone"]
        }

    return None

# print("user['email']: ", user["email"])
# print("user['name']['first']+" "+user['name']['last']:", user["name"]["first"]+" "+user["name"]["last"])
# print("user['login']['password'] : ", user["login"]["password"])
# print("user['phone'] : ", user["phone"])

