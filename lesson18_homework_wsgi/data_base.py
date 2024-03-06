import psycopg2


def data_from_db():
    connection = psycopg2.connect(user='travel_user', password='travel', host='localhost', database='travel_db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    cursor.execute('SELECT * FROM country')
    countries = cursor.fetchall()
    cursor.execute('SELECT * FROM userscountry')
    userscountry = cursor.fetchall()
    users_list = []
    for user in users:
        countries_list = []
        user_id = user[1]
        name = user[2]
        email = user[3]
        age = user[4]
        for user_countries in userscountry:
            if user_id == user_countries[0]:
                for country in countries:
                    if country[1] == user_countries[1]:
                        countries_list.append(country[2])
        users_list.append({"user_id": user_id, "name": name, "email": email, "age": age, "countries": countries_list})
    return users_list
