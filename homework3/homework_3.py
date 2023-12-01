#1
def return_list():
    it_is_false = False
    list_1 = [int(it_is_false), int(not it_is_false),int(str(len(str(int(it_is_false)))) + str(int(it_is_false)))]
    return (list_1)
print("return_list - ", return_list())

it_is_false = False
list_1 = [int(it_is_false), int(not it_is_false),int(str(len(str(int(it_is_false)))) + str(int(it_is_false)))]
print("list_1 - ", list_1)

#2
def get_password():
    password = input('Enter password > ')
    return password
def check_password(password):
    if 2 > len(password):
        print("Error. The password is too short. The name must contain more than 1 character.")
    elif 10 < len(password):
        print("Error. The password is too long. The name must contain less than 11 characters.")
    else:
        return password

password = check_password(get_password())
if password:
    print(f"You password - {password}")

#2*
def check_name():
    for user in users:
        if name == user[0]:
            return True

def check_password():
    for user in users:
        if name == user[0]:
            if password == user[1]:
                return True

def get_name():
    name = input("Enter your name \n")
    return name

def get_password():
    password = input("Enter your password \n")
    return password


users = [("victor", "password123"), ("john", "pass321"), ("peter", "12345"), ("donald", "54321"), ("jack", "123")]

name = None
while name != "exit" :
    name = get_name()
    password = get_password()

    if check_name():
        if check_password():
            print(f"Hey {name}!")
            break

    print("Authentication Error. Check name or password!")

#2* Variant with dict
def convertation_list_dict(list):
    db_dict = {}
    for user in list:
        db_dict[user[0]] = user[1]
    return db_dict

def check_name():
    if name in users_db.keys():
        return True

def check_password():
    if password == users_db[name]:
        return True

def get_name():
    name = input("Enter your name \n")
    return name

def get_password():
    password = input("Enter your password \n")
    return password

users = [("victor", "password123"), ("john", "pass321"), ("peter", "12345"), ("donald", "54321"), ("jack", "123")]
users_db = convertation_list_dict(users)

name = None
while name != "exit" :
    name = get_name()
    if name == "exit":
        print("bye ")
        break
    password = get_password()

    if check_name():
        if check_password():
            print(f"Hey {name}!")
            break

    print("Authentication Error. Check name or password!")

    # HomeWork3 № 2*
    users = [("victor", "password123"), ("john", "pass321"), ("peter", "12345"), ("donald", "54321"), ("jack", "123")]


    def get_name():
        name = input('Enter name > ')
        return name


    def check_name(name):
        if 2 > len(name):
            print("Error. The name is too short. The name must contain more than 1 character.")
        elif 10 < len(name):
            print("Error. The name is too long. The name must contain less than 11 characters.")
        else:
            return name


    def get_password():
        password = input('Enter password > ')
        return password


    def check_password(password):
        if 2 > len(password):
            print("Error. The password is too short. The name must contain more than 1 character.")
        elif 10 < len(password):
            print("Error. The password is too long. The name must contain less than 11 characters.")
        else:
            return password


    while True:
        name = get_name()
        password = get_password()

        if check_name(name):
            if check_password(password):
                print(f"Hey {name}!")
                break

        print("Authentication Error. Check name or password!")
