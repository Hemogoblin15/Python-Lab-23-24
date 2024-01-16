from sqlalchemy import exc
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

from db.db_connection import *


@contextmanager
def session_scope():
    """
    Creates a session which is bound to the engine(from the Database class),used to execute queries.
    """
    connection = Database.get_instance()
    engine = connection.engine
    Session = sessionmaker(bind=engine)
    session = Session()
    # try:
    yield session
    session.commit()
