from sqlalchemy import Column, Integer, String, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

"""
    Class representing a TV series made after the model in the database.

    Attributes

    id : int
        serial primary key, the id of each TV series in the database.
    name : varchar
        the TV series' name
    link_imdb : varchar
        link to the TV series' IMDb page
    rating : float
        rating set by the user for a TV series
    last_watched_episode : string
        the last watched episode of a TV series
    last_time_watched : date
        the last time the user's watched a specific TV series
    snoozed : bool
        boolean flag to have notifications turned on/off.   true means snoozed = notifications off
                                                            false means unsnoozed = notifications on 
                                                            
    Functions 
    
    
    """


class Series(Base):
    __tablename__ = 'series'
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String, nullable=False)
    link_imdb = Column("link_imdb", String, nullable=False)
    rating = Column("rating", Integer, nullable=True)
    last_watched_episode = Column("last_watched_episode", String, nullable=True)
    last_time_watched = Column("last_time_watched", Date, nullable=True)
    snoozed = Column("snoozed", Boolean, default=False)

    """
    Constructor for a Series object. Takes as parameter the name of the series that is bound to become an instance of 
    the class
    """

    def __init__(self, name):
        self.id = None
        self.name = name
        self.link_imdb = None
        self.last_watched_episode = None
        self.last_time_watched = None
        self.rating = None
