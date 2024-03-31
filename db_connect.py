from sqlalchemy import (create_engine, MetaData, Table,
                        Column, String, Float, JSON,
                        insert, update)


class ConnectDb:
    """
    ConnectDb - forms connection to database.
    """

    db_url = 'mysql+mysqlconnector://jjbush_admin:ANo9Eju{_&4-.V+8Z%OP@webdb.uvm.edu/JJBUSH_sports_book'
    connection = 'default'
    user_info = 'empty table'

    def __init__(self):
        try:
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
        except Exception as e:
            print('ERROR: Cannot connect to database with error: '+str(e))

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

    def does_user_exist(self, username) -> bool:
        """
        Checks if a given username exists in the db
        :param username: str
        :return: bool
        """
        rows = self.get_row_by_user(username)
        if (rows != None):
            return True
        return False

    def add_new_user(self, username, password, balance=20, active_bets=None, resolved_bets=None) -> int:
        """
        :param username:
        :param password:
        :param balance:
        :param active_bets:
        :param resolved_bets:
        :return: 0 if the user is added successfully, 1 if the user already exists,
        2 if user doesn't exist but is not added
        """
        # Check that username does not already exist
        if not self.does_user_exist(username):
            return 1

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
        if self.does_user_exist(username):
            return 0
        return 2

    def edit_row(self, username, field_to_update, updated_value) -> int:
        """
        Edits the desired column of the user given
        :param username:
        :param field_to_update:
        :param updated_value:
        :return: int 0 if sucessful
        """
        # Check if user exits
        if not self.does_user_exist(username):
            return 1

        upd = update(self.user_info)
        item_to_update = upd.values({field_to_update: updated_value})
        update_query = item_to_update.where(self.user_info.c.username == username)
        self.connection.execute(update_query)
        self.connection.commit()

        return 0

