# validators.py

def check_data(email, password, users):
    for account in users:
        if account['email'] == email and account['password'] == password:
            return email
    return 'Your data is wrong'
