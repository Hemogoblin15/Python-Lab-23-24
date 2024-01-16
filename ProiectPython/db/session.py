from sqlalchemy import exc
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

from db.db_connection import *


@contextmanager
def session_scope():
    """
    Makes a Session object binding to the engine and making it able to send and resolve queries.
    """
    connection = Database.get_instance()
    engine = connection.engine
    Session = sessionmaker(bind=engine)
    session = Session()
    # try:
    yield session
    session.commit()
