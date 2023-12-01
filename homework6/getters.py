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
