import sqlalchemy as sa
import psycopg2

engine = sa.create_engine('postgresql+psycopg2://python:123@localhost:5432/products')

metadata = sa.MetaData()

products = sa.Table('products', metadata,
                    sa.Column('id', sa.Integer, primary_key=True),
                    sa.Column('name', sa.String, nullable=False),
                    sa.Column('calories', sa.Integer),
                    sa.Column('protein', sa.Integer),
                    sa.Column('fat', sa.Integer),
                    sa.Column('carbs', sa.Integer)
                    )

metadata.create_all(engine)


def add_product(product):
    conn = engine.connect()
    conn.execute(products.insert(), product)
    conn.close()


def delete_product(name):
    conn = engine.connect()
    conn.execute(products.delete().where(products.c.name == name))
    conn.close()


def get_product(name):
    conn = engine.connect()
    result = conn.execute(products.select().where(products.c.name == name))
    row = result.fetchone()
    conn.close()
    if row:
        product = dict(row)
        return product
