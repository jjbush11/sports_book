from sqlalchemy import (create_engine, MetaData, Table,
                        Column, String, Float, JSON,
                        insert, update, Date, Integer)


class ConnectDbMatch:
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

            # Define metadata
            # metadata = MetaData()

            # Set up sport table framework
            # self.past_match_up = Table(
            #     'sport_info',
            #     metadata,
            #     Column('id', String(30), primary_key=True),
            #     Column('date', Date(30)),
            #     Column('winning_team', String(20)),
            #     Column('winning_score', Integer(3)),
            #     Column('losing_team', String(20)),
            #     Column('losing_score', Integer(3)),
            # )

            metadata_upcoming = MetaData()
            # Set up sport table framework
            self.upcoming_matches = Table(
                'upcoming_matches',
                metadata_upcoming,
                Column('id', String(30), primary_key=True),
                Column('team1', String(30)),
                Column('team1_odds', Integer),
                Column('team2', String(30)),
                Column('team2_odds', Integer)
            )

        except Exception as e:
            print('ERROR: Cannot connect to database with error: ' + str(e))

    # Closing connection
    def __del__(self):
        self.connection.close()

        # Instance method (operate on instance attributes, can also access class attributes)

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

    def add_new_upcoming_match(self, id, team1, team1_odds, team2, team2_odds) -> int:
        """
        Add new upcoming match up
        :param id:
        :param team1:
        :param team1_odds:
        :param team2:
        :param team2_odds:
        :return:
        """
        # Check that username does not already exist
        if self.get_upcoming_matches_by_id(id):
            return 1

        # Create a new user object with the provided data
        new_match_up = insert(self.upcoming_matches).values(
            id=id,
            team1=team1,
            team1_odds=team1_odds,
            team2=team2,
            team2_odds=team2_odds
        )

        # Insert the new user into the user_info table
        print(self.connection.execute(new_match_up))
        self.connection.commit()

        # Check if user was added
        if self.get_upcoming_matches_by_id(id):
            return 0
        return 2

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
