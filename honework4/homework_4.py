users = [
    {
        "name": "Victor",
        "age": 24,
        "is_working": False,
        "citizenship": ["Russian", "England"]
    }
]
age_for_check = 20

#1.1
def print_name_age(db):
    for user in db:
        name = user["name"]
        age = user["age"]
        print(f"{name} is {age} years old")

#1.1 v2
def print_name_age(db):
    for user in db:
        print(f"{user['name']} is {user['age']} years old")


print_name_age(users)

#1.2
def print_name_age_older_18(db):
    for user in db:
        name = user["name"]
        age = user["age"]
        if age >= 18:
            print(f"{name} is {age} years old")


print_name_age_older_18(users)

#1.2*
def print_name_age_older_x(db, checked_age):
    for user in db:
        name = user["name"]
        age = user["age"]
        if age >= checked_age:
            print(f"{name} is {age} years old")


print_name_age_older_x(users, age_for_check)

#1.3
def print_name_citizenship(db):
    dict1 = {}
    for user in db:
        dict1[user["name"]]= user["citizenship"]
    print (dict1)

print_name_citizenship(users)

#1.4
def new_users_dict(db):
    list1 = []
    for user in db:
        if user["age"] < 18 and  user["is_working"] or user["age"] >= 18 and not user["is_working"]:
            user["status"]= "suspicious"
        elif user["age"] < 18 and not user["is_working"] or user["age"] >= 18 and user["is_working"]:
            user["status"]= "not_suspicious"
        list1.append(user)
    return list1

print(new_users_dict(users))