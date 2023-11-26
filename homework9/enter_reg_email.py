import json


def database_file():  # this function return name of database file
    return 'users_database.json'


def input_operation():
    choice = input('for authentication input 1\nfor registration input 2\n for exit input 3\n')
    if choice in ('1', '2', '3'):
        return choice
    print('your input is wrong')


def get_mail():
    email = input('enter you email ')
    return email


def get_password():
    password = input('enter you password ')
    return password


def check_email(email, database):
    for account in database:
        if account['email'] == email:
            return True
    return False


def check_password(email, password, database):
    for account in database:
        if account['email'] == email and account['password'] == password:
            return True
    return False


def authentication():
    database = read_database()
    if not database:
        return False
    email = get_mail()
    password = get_password()
    if check_password(email, password, database):
        print('authentication is OK')
        quit()
    print('incorrect email or password')


def registration():
    while True:
        email = get_mail()
        password = get_password()
        if len(email) > 2 and len(password) > 2:
            print('please enter your password again')
            if get_password() == password:
                new_data = {'email': email, 'password': password}
                if write_database(new_data):
                    return True
                else:
                    return False
            print('the entered passwords do not match')
        else:
            print('email or password is too short (must be more then 2 characters)')


def read_database():
    try:
        with open(f'{database_file()}') as file:
            database = json.load(file)
        return database
    except FileNotFoundError:
        print('no one user is not registred please go to registration and try again')


def write_database(new_data):
    try:
        with open(f'{database_file()}') as file:
            database = json.load(file)
        if check_email(new_data['email'], database):
            return False
    except FileNotFoundError:
        database = []
    database.append(new_data)
    with open(f'{database_file()}', 'w') as file:
        json.dump(database, file)
    return True


def app():
    while True:
        operation = input_operation()
        if operation == '1':
            authentication()
        elif operation == '2':
            if registration():
                print('your registration is OK')
            else:
                print('this email is busy you can try to authentication or registration with other email')
        elif operation == '3':
            print('bye-bye')
            quit()


app()
