from sqlalchemy import create_engine
from sqlalchemy.orm import Session

ssl_args = {'ssl': {'ca': '/etc/pki/tls/certs/webdb-cacert.pem'}}
db_engine = create_engine(
        'mysql://jjbush:Madden25jjbush@webdb.uvm.edu/mydbname',
        connect_args=ssl_args)
Session = sessionmaker(bind=db_engine)
db = Session()
