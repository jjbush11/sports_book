from sqlalchemy import (create_engine, MetaData, Table,
                        Column, String, Float, JSON,
                        insert, update, Date, Integer,
                        Boolean, Time, select, delete)
import datetime


class ConnectDbUpcomingMatch:
    """
    ConnectDb - forms connection to database.
    """

    db_url = 'mysql+mysqlconnector://jjbush_admin:ANo9Eju{_&4-.V+8Z%OP@webdb.uvm.edu/JJBUSH_sports_book'
    connection = 'default'
    upcoming_match_up = 'sport empty table'

    def __init__(self):
        try:
            # Create engine and connect
            db_engine = create_engine(self.db_url)
            self.connection = db_engine.connect()

            metadata_upcoming = MetaData()
            # Set up sport table framework
            self.upcoming_matches = Table(
                'upcoming_matches',
                metadata_upcoming,
                Column('id', String(30), primary_key=True),
                Column('home', String(30)),
                Column('home_odds', Integer),
                Column('away', String(30)),
                Column('away_odds', Integer),
                Column('date', Date),
                Column('time', Time)
            )

        except Exception as e:
            print('ERROR: Cannot connect to database with error: ' + str(e))

    # Closing connection
    def __del__(self):
        self.connection.close()

    def get_all_matches(self):
        """
        Gets all upcoming matches in the database
        :return: list of all matches
        """
        try:
            query = self.upcoming_matches.select().where(self.upcoming_matches.c.id != 'null')
            result = self.connection.execute(query)
            rows = result.fetchall()

            return rows
        except:
            return None

    def get_upcoming_matches_by_id(self, par_id):
        """
        Takes id and returns the row of the match up
        :param: par_id, str
        :return: if match up found returns all info
        if match up not found returns None
        """
        try:
            query = self.upcoming_matches.select().where(self.upcoming_matches.c.id == par_id)
            result = self.connection.execute(query)
            rows = result.fetchall()[0]

            return rows
        except:
            return None

    def does_upcoming_match_exist(self, par_id) -> bool:
        """
        Checks if a given id exists in the db
        :param par_id: str
        :return: bool
        """
        rows = self.get_upcoming_matches_by_id(par_id)
        if rows != None:
            return True
        return False

    def add_new_upcoming_match(self, id, home, home_odds, away, away_odds, date, time) -> int:
        """
        Add new upcoming match up
        :param id:
        :param home:
        :param home_odds:
        :param away:
        :param away_odds:
        :return:
        """
        # Check that username does not already exist
        if self.get_upcoming_matches_by_id(id):
            return 1

        # Create a new user object with the provided data
        new_match_up = insert(self.upcoming_matches).values(
            id=id,
            home=home,
            home_odds=home_odds,
            away=away,
            away_odds=away_odds,
            date=date,
            time=time
        )

        # Insert the new user into the user_info table
        print(self.connection.execute(new_match_up))
        self.connection.commit()

        # Check if user was added
        if self.get_upcoming_matches_by_id(id):
            return 0
        return 2

    def remove_upcoming_match(self, par_id):
        """
        Removes upcoming match by id
        :param par_id: str
        :return: 0 is removed, 1 if id does not exist
        """
        # Check that username does not already exist
        if not self.get_upcoming_matches_by_id(par_id):
            return 1

        # Generates delete query
        del_query = delete(self.upcoming_matches).where(self.upcoming_matches.c.id == par_id)

        # Executes delete query
        self.connection.execute(del_query)
        self.connection.commit()

        return 0

    def remove_all(self):
        """
        Removes all upcoming matches from database
        :return: 0 if successful
        """
        # Generates delete query
        del_query = delete(self.upcoming_matches).where(self.upcoming_matches.c.id != "null")

        # Executes delete query
        self.connection.execute(del_query)
        self.connection.commit()

        return 0

    def edit_upcoming_match_row(self, id, field_to_update, updated_value) -> int:
        """
        Edits the desired column of the user given
        :param username:
        :param field_to_update:
        :param updated_value:
        :return: int 0 if sucessful
        """
        # Check if user exits
        if not self.get_upcoming_matches_by_id(id):
            return 1

        upd = update(self.upcoming_matches)
        item_to_update = upd.values({field_to_update: updated_value})
        update_query = item_to_update.where(self.upcoming_matches.c.id == id)
        self.connection.execute(update_query)
        self.connection.commit()

        return 0
