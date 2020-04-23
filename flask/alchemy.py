from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

engine = create_engine('sqlite:///mydata.sql', echo=True)
# engine = create_engine('postgres://user:pass@localhost:5432/mydb', echo=True)

metadata = MetaData()
users = Table('users', metadata,
      Column('id', Integer, primary_key=True),
      Column('name', String),
      Column('fullname', String),
)

addresses = Table('addresses', metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', None, ForeignKey('users.id')),
    Column('email_address', String, nullable=False)
)

food = Table('food', metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', None, ForeignKey('users.id')),
    Column('favourite_food', String, nullable=False)
)


metadata.create_all(engine)
