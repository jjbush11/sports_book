from sqlalchemy import (create_engine, MetaData, Table,
                        Column, String, Float, JSON,
                        insert, update, Date, Integer,
                        Boolean, Time, select, delete)
import datetime


class ConnectDbSettledMatch:
    """
    ConnectDb - forms connection to database.
    """

    db_url = 'mysql+mysqlconnector://jjbush_admin:ANo9Eju{_&4-.V+8Z%OP@webdb.uvm.edu/JJBUSH_sports_book'
    connection = 'default'
    settled_match_up = 'sport empty table'

    def __init__(self):
        try:
            # Create engine and connect
            db_engine = create_engine(self.db_url)
            self.connection = db_engine.connect()

            metadata_settled = MetaData()
            # Set up sport table framework
            self.settled_matches = Table(
                'settled_matches',
                metadata_settled,
                Column('id', String(30), primary_key=True),
                Column('away', String(30)),
                Column('away_score', Integer),
                Column('home', String(30)),
                Column('home_score', Integer),
                Column('sport', String(40))
            )

        except Exception as e:
            print('ERROR: Cannot connect to database with error: ' + str(e))

    # Closing connection
    def __del__(self):
        self.connection.close()

    def get_all_matches(self):
        """
        Gets all settled matches in the database
        :return: list of settled matches
        """
        try:
            query = self.settled_matches.select().where(self.settled_matches.c.id != 'null')
            result = self.connection.execute(query)
            rows = result.fetchall()

            return rows
        except:
            return None

    def get_settled_matches_by_id(self, par_id):
        """
        Takes id and returns the row of the match up
        :param: par_id, str
        :return: if match up found returns all info
        if match up not found returns None
        """
        try:
            query = self.settled_matches.select().where(self.settled_matches.c.id == par_id)
            result = self.connection.execute(query)
            rows = result.fetchall()[0]

            return rows
        except:
            return None

    def does_settled_match_exist(self, par_id) -> bool:
        """
        Checks if a given id exists in the db
        :param par_id: str
        :return: bool
        """
        rows = self.get_settled_matches_by_id(par_id)
        if rows != None:
            return True
        return False

    def add_new_settled_match(self, par_id, away, away_score, home, home_score, sport) -> int:
        """
        Add new settled match up
        :param par_id: str
        :param away: str
        :param away_score: int
        :param home: str
        :param home_score: int
        :param sport: str
        :return: int, 1 if match already exits, 0 if added successfully, 2 if not added
        """
        # Check that username does not already exist
        if self.get_settled_matches_by_id(par_id):
            return 1

        # Create a new user object with the provided data
        new_match_up = insert(self.settled_matches).values(
            id=par_id,
            away=away,
            away_score=away_score,
            home=home,
            home_score=home_score,
            sport=sport
        )

        # Insert the new user into the user_info table
        self.connection.execute(new_match_up)
        self.connection.commit()

        # Check if user was added
        if self.get_settled_matches_by_id(par_id):
            return 0
        return 2

    def remove_settled_match(self, par_id):
        """
        Removes settled match by id
        :param par_id: str
        :return: 0 is removed, 1 if id does not exist
        """
        # Check that username does not already exist
        if not self.get_settled_matches_by_id(par_id):
            return 1

        # Generates delete query
        del_query = delete(self.settled_matches).where(self.settled_matches.c.id == par_id)

        # Executes delete query
        self.connection.execute(del_query)
        self.connection.commit()

        return 0

    def remove_all(self):
        """
        Removes all settled matches from database
        :return: 0 if successful
        """
        # Generates delete query
        del_query = delete(self.settled_matches).where(self.settled_matches.c.id != "null")

        # Executes delete query
        self.connection.execute(del_query)
        self.connection.commit()

        return 0

    def edit_settled_match_row(self, par_id, field_to_update, updated_value) -> int:
        """
        Edits the desired column of the user given
        :param par_id: str
        :param field_to_update: str
        :param updated_value:
        :return: int 0 if successful
        """
        # Check if user exits
        if not self.get_settled_matches_by_id(par_id):
            return 1

        upd = update(self.settled_matches)
        item_to_update = upd.values({field_to_update: updated_value})
        update_query = item_to_update.where(self.settled_matches.c.id == par_id)
        self.connection.execute(update_query)
        self.connection.commit()

        return 0
