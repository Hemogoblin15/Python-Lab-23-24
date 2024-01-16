from sqlalchemy import create_engine
from db.db_settings import postgresql


class Database:
    """
    The class that handles the database connection
    Attributes

    connection : Database
                provides database connection

    engine : Engine
           instance of Engine class, helps the connectivity

    Functions

    get_instance()
        Returns the specific instance of the database class.
    """
    connection = None

    @staticmethod
    def get_instance():
        """
        Returns a specific instance of the database class.

        :return: a specific instance of the database class
        """
        if Database.connection is None:
            Database()
        return Database.connection

    def __init__(self):
        """
        Private constructor. Creates the database connection.
        The parameters used are provided by the db_settings.py file
        """
        if Database.connection is not None:
            raise Exception("Error! Creating more instances of a singleton is not allowed")
        else:
            Database.connection = self
            url = 'postgresql://{user}:{passwd}@{host}:{port}/{db}'.format(
                user=postgresql['pguser'], passwd=postgresql['pgpasswd'], host=postgresql['pghost'],
                port=postgresql['pgport'], db=postgresql['pgdb'])
            try:
                self.engine = create_engine(url, pool_size=50)
                print("Connected to PostgreSQL database!")
            except IOError:
                print("Failed to connect to the database.")
