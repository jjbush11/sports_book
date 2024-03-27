

from sqlalchemy import create_engine, MetaData, Table, Column, String, Float, JSON, and_, insert, text
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

    print("*******Add User**********\n")

    # Insert data into the table
    insert_info = {
        'username': 'john_doe',
        'password': 'password123',
        'balance': 1000.0,
        'active_bets': [{'bet_id': 1, 'amount': 50.0}, {'bet_id': 2, 'amount': 75.0}],
        'resolved_bets': []
    }

    # insert_info2 = (
    #     username= 'john_doe',
    #     password='password123',
    #     balance= 1000.0,
    #     active_bets= [{'bet_id': 1, 'amount': 50.0}, {'bet_id': 2, 'amount': 75.0}],
    #     resolved_bets= []
    # )

    # Insert data into the table
    # insert_statement = str(user_info.insert().values(insert_info))
    insert_statement = """
    INSERT INTO user_info (username, password, balance, active_bets, resolved_bets) 
    VALUES (:username, :password, :balance, :active_bets, :resolved_bets)
    """
    # insert_edit = ''
    # for key, value in insert_info.items():
    #     word_to_replace = ':'+key
    #     insert_statement+= insert_statement.replace(word_to_replace, str(insert_info[key]))

    # insert_statement = text(insert_statement_str).bindparams(username='john_doe', password='password123',
    #                                                          balance=1000.0, active_bets=[{'bet_id': 1, 'amount': 50.0}, {'bet_id': 2, 'amount': 75.0}],
    #                                                          resolved_bets=[])
    insert2 = insert(user_info).values(
        username='letsGooo',
        password='password123',
        balance=210.0,
        active_bets=[{'bet_id': 1, 'amount': 50.0}, {'bet_id': 2, 'amount': 75.0}],
        resolved_bets=[]
    )
    # print(insert2.compile())
    # insert_statement.replace(':username', insert_info['username']))
    # # Execute the insert statement
    connection.execute(insert2)
    connection.commit()

    # Close the connection
    connection.close()
except Exception as e:
    # Print error message if connection fails
    print("Error:", e)
