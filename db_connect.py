from sqlalchemy import (create_engine, MetaData, Table,
                        Column, String, Float, JSON, and_,
                        insert)


class ConnectDb:
    """
    ConnectDb - forms connection to database.
    """

    db_url = 'mysql+mysqlconnector://jjbush_admin:ANo9Eju{_&4-.V+8Z%OP@webdb.uvm.edu/JJBUSH_sports_book'
    connection = 'default'
    user_info = 'empty table'

    def __init__(self):
        # Create engine and connect
        db_engine = create_engine(self.db_url)
        self.connection = db_engine.connect()

        # Define metadata
        metadata = MetaData()

        # Set up table framework
        self.user_info = Table(
            'user_info',
            metadata,
            Column('username', String(30), primary_key=True),
            Column('password', String(30)),
            Column('balance', Float),
            Column('active_bets', JSON),
            Column('resolved_bets', JSON)
        )

    # Closing connection
    def __del__(self):
        self.connection.close()

        # Instance method (operate on instance attributes, can also access class attributes)
    def get_row_by_user(self, par_user):
        """
        Takes username and returns the row of the user
        :param: par_user, str
        :return: if user found returns user info
        if user not found returns None
        """
        try:
            query = self.user_info.select().where(self.user_info.c.username == par_user)
            result = self.connection.execute(query)
            rows = result.fetchall()[0]

            return rows
        except:
            return None

    def add_new_user(self, username, password, balance=20, active_bets=None, resolved_bets=None):

        # Check that username does not already exist

        # Create a new user object with the provided data
        new_user = insert(self.user_info).values(
            username= username,
            password= password,
            balance= balance,
            active_bets= active_bets,
            resolved_bets= resolved_bets
        )

        # Insert the new user into the user_info table
        self.connection.execute(new_user)
        self.connection.commit()

        # Check if user was added
        rows = self.get_row_by_user(username)
        if (rows!=None):
            return True
        return False
