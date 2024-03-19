from sqlalchemy import create_engine, MetaData, Table, Column, String, Float, JSON, and_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database URL
#?server_version=8.0.36-28
db_url = 'mysql+mysqlconnector://jjbush_admin:ANo9Eju{_&4-.V+8Z%OP@webdb.uvm.edu/JJBUSH_sports_book'

try:
    # Create engine and connect
    db_engine = create_engine(db_url)
    connection = db_engine.connect()

    # Print connection status
    print("Database connection successful!")

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

    query = user_info.select().where(user_info.c.username == 'jamesBush')
    print(query)
    result = connection.execute(query)
    rows = result.fetchall()

    for row in rows:
        print(row)

    # Close the connection
    connection.close()
except Exception as e:
    # Print error message if connection fails
    print("Error:", e)
