from sqlalchemy import (create_engine, MetaData, Table,
                        Column, String, Float, JSON,
                        insert, update, Date, Integer,
                        Boolean, Time, select, delete)
from bet import Bet
import datetime


class ConnectDbBet:
    """
    ConnectDb - forms connection to database.
    """

    db_url = 'mysql+mysqlconnector://jjbush_admin:ANo9Eju{_&4-.V+8Z%OP@webdb.uvm.edu/JJBUSH_sports_book'
    connection = 'default'
    bet_table = 'sport empty table'

    def __init__(self):
        try:
            # Create engine and connect
            db_engine = create_engine(self.db_url)
            self.connection = db_engine.connect()

            metadata_bet = MetaData()
            # Set up sport table framework
            self.bet_table = Table(
                'bet_table',
                metadata_bet,
                Column('username', String(40)),
                Column('id', String(60), primary_key=True),
                Column('win', Boolean),
                Column('odds', Integer),
                Column('wager', Integer),
                Column('return_val', Float)
            )

        except Exception as e:
            print('ERROR: Cannot connect to database with error: ' + str(e))

    # Closing connection
    def __del__(self):
        self.connection.close()

    def get_all_bet(self):
        try:
            query = self.bet_table.select().where(self.bet_table.c.id != 'null')
            result = self.connection.execute(query)
            rows = result.fetchall()

            return rows
        except:
            return None

    def get_bet_by_id(self, par_id):
        """
        Takes id and returns the row of the bet up
        :param: par_id, str
        :return: if bet up found returns all info
        if bet up not found returns None
        """
        try:
            query = self.bet_table.select().where(self.bet_table.c.id == par_id)
            result = self.connection.execute(query)
            rows = result.fetchall()[0]

            return rows
        except:
            return None

    def does_bet_exist(self, par_id) -> bool:
        """
        Checks if a given id exists in the db
        :param par_id: str
        :return: bool
        """
        rows = self.get_bet_by_id(par_id)
        if rows != None:
            return True
        return False

    def add_new_bet(self, username, bet) -> int:
        """
        Add new settled bet up
        :param bet: Bet object
        :param username: str
        :return: int, 1 if bet already exits, 0 if added successfully, 2 if not added
        """
        # Check that username does not already exist
        if self.get_bet_by_id(bet.id):
            return 1

        # Create a new user object with the provided data
        new_bet = insert(self.bet_table).values(
            id=bet.id,
            username=username,
            win=bet.win,
            odds=bet.odds,
            wager=bet.wager,
            return_val=bet.return_val
        )

        # Insert the new user into the user_info table
        self.connection.commit()

        # Check if user was added
        if self.get_bet_by_id(bet.id):
            return 0
        return 2

    def remove_bet(self, par_id):
        """
        :param par_id: str
        """
        # Check that username does not already exist
        if not self.get_bet_by_id(par_id):
            return 1

        # Generates delete query
        del_query = delete(self.bet_table).where(self.bet_table.c.id == par_id)

        # Executes delete query
        self.connection.execute(del_query)
        self.connection.commit()

    def edit_bet_row(self, par_id, field_to_update, updated_value) -> int:
        """
        Edits the desired column of the user given
        :param par_id: str
        :param username: str
        :param field_to_update: str
        :param updated_value:
        :return: int 0 if successful
        """
        # Check if user exits
        if not self.get_bet_by_id(par_id):
            return 1

        upd = update(self.bet_table)
        item_to_update = upd.values({field_to_update: updated_value})
        update_query = item_to_update.where(self.bet_table.c.id == par_id)
        self.connection.execute(update_query)
        self.connection.commit()

        return 0
