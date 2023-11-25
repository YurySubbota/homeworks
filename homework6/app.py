# app.py
from getters import get_mail, get_password, data_base
from validators import check_data


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
