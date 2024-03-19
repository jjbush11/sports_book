from sqlalchemy import create_engine, MetaData, Table, Column, String, Float, JSON, and_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

ssl_args = {'ssl': {'ca': '/etc/pki/tls/certs/webdb-cacert.pem'}}
db_engine = create_engine(
    'mysql://jjbush:Madden25jjbush@webdb.uvm.edu/JJBUSH_sports_book',
    connect_args=ssl_args)
# Session = sessionmaker(bind=db_engine)
# db = Session()


Base = declarative_base()


class UserInfo(Base):
    __tablename__ = 'user_info'

    username = Column(String(30), primary_key=True)
    password = Column(String(30))
    balance = Column(Float)
    active_bets = Column(JSON)
    resolved_bets = Column(JSON)


# Create session
Session = sessionmaker(bind=db_engine)
db = Session()

# Query
query = db.query(UserInfo).filter(UserInfo.balance == 20).all()

if query:
        print(query)
        # print("pass " + query.password)

# with db_engine.connect() as connection:
#     print("connect")
#     # result = connection.execute(query)
#     # rows = result.fetchall()
# for user in query:
#     print(f"Username: {user.username}, Balance: {user.balance}")

# Close the session
db.close()
