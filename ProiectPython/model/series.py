from sqlalchemy import Column, Integer, String, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


"""
    Class that represents the a tv show.

    Attributes
    ----------
    id : int
        the id of the tv show in the database
    title : str
        the title of the tv show
    link : str
        link to the tv show's imdb page
    last_episode : int
        the last watched episode
    last_date : date
        the date when the last episode was seen
    score : int
        the user score for the tv show
    snoozed : bool
        true if a show is snoozed,false otherwise
    """
class Series(Base):

    __tablename__ = 'series'
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String, nullable=False)
    link_imdb = Column("link_imdb", String, nullable=False)
    rating = Column("rating", Integer, nullable=True)
    last_watched_episode = Column("last_watched_episode", Integer, nullable=True)
    last_time_watched = Column("last_time_watched", Integer, nullable=True)
    snoozed = Column("snoozed", Boolean, default=False)

    def __init__(self, name):
        self.id = None
        self.name = name
        self.link_imdb = None
        self.last_watched_episode = None
        self.last_time_watched = None
        self.rating = None
