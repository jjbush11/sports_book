from sqlalchemy import create_engine, MetaData, Table, Column, String, Float, JSON, and_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create a SQLAlchemy engine
ssl_args = {'ssl': {'ca': '/etc/pki/tls/certs/webdb-cacert.pem'}}
db_engine = create_engine(
    'mysql://jjbush:Madden25jjbush@webdb.uvm.edu/JJBUSH_sports_book',
    connect_args=ssl_args)

Session = sessionmaker(bind=db_engine)
db = Session()

# Define metadata
metadata = MetaData()

user_info = Table(
    'user_info',
    metadata,
    Column('username', String(30), primary_key=True),
    Column('password', String(30)),
    Column('balance', Float),
    Column('active_bets', JSON),
    Column('resolved_bets', JSON)
)

query = user_info.select().where(user_info.c.balance == 20.0)
print(query)

# Execute the query
with db_engine.connect() as connection:
    print("connect")
    result = connection.execute(query)
    rows = result.fetchall()

# Process the query results
# for row in rows:
#     print(row)
