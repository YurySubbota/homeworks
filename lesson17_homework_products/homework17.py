import psycopg2
connection = psycopg2.connect(user='subbota', password='subota', host='localhost', database='products')
cursor = connection.cursor()
product = []
for i in 'name', 'proteins', 'fats', 'carbohydrates':
    product.append(input(f'input {i}'))

cursor.execute('INSERT INTO users (name, proteins, fats, carbohydrates) '
               'VALUES (%s, %s, %s, %s)',
               product)
connection.commit()
cursor.close()
connection.close()