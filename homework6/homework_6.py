# getters.py

def get_mail():
    email = input('enter you email ')
    if email == 'exit':
        print('bye - bye')
        quit()
    return email


def get_password():
    password = input('enter you password ')
    return password


def data_base():
    users = [{'email': 'some@mail.ru', 'password': '123pass'}, {'email': 'some2@mail.ru', 'password': '12345'}]
    return users


# validators.py

def check_data(email, password, users):
    for account in users:
        if account['email'] == email and account['password'] == password:
            return email
    return 'Your data is wrong'


# app.py
# from getters import get_mail, get_password, data_base
# from validators import check_data


def app():
    while True:
        print(check_data(get_mail(), get_password(), data_base()))


app()

'''
def app():
    while True:
        email = get_mail()
        password = get_password()
        users = data_base()
        check = check_data(email, password, users)
        print(check)
'''
