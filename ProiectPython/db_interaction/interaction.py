from model.series import Series
from sqlalchemy import exc, func
from utils.imdb_crawler import find_imdb_link
import datetime
from plyer import notification


class Interaction:
    """
    A class to represent the database interaction.

    ...
    Attributes
    ----------
    session:
        database session on which all the queries will take place

    Methods
    -------
    insert_series(series):
        Adds a new tv series to the database.
    delete_series(series_name):
        Deletes a tv series from the database.
    get_all_series():
        Returns a list of all the tv series from the database.
    get_all_usnoozed_series():
        Returns a list of all the series that are not snoozed from the database.
    update_last_watched_episode(series_name, episode, season):
        Updates the last watched episode for a certain tv series.
    update_last_watched_date(series_name, date):
        Updates the last watched date for a certain tv series.
    update_rating(series_name, rating):
        Updates the rating for a certain tv series.
    snooze_series(series_name):
        Sets the series on snooze.
    unsnooze_series(series_name):
        Sets the series on unsnooze.
    get_last_seen_episode(series_name):
        Returns the last seen episode for a certain series.
    is_series_in_db(series_name):
        Returns a boolean value if the series is in the database or not.
    """

    def __init__(self, session):
        """
        Constructor.
        :param session:
            database session on which all the queries will take place
        """
        self.session = session

    def insert_series(self, series: Series):
        """
        Adds a new tv series to the database.
        :param series: a tv series object that will be added to the database
        :return: None
        """
        series.link_imdb = find_imdb_link(series.name)
        try:
            self.session.add(series)
            self.session.commit()
            print(f'series added successfully.')
        except exc.SQLAlchemyError:
            self.session.rollback()
            raise Exception("Could not add series. Rollback done.")

    def delete_series(self, series_name):
        """
        Deletes a tv series from the database.
        :param series_name: the name of the series that is going to be deleted
        :return: None
        """
        try:
            self.session.query(Series).filter(func.lower(Series.name) == series_name.lower()). \
                delete(synchronize_session=False)
            self.session.commit()
            print("series deleted successfully")
        except exc.SQLAlchemyError:
            print(exc)
            self.session.rollback()
            raise Exception("Could not delete the series.Rollback done!")

    def get_all_series(self):
        """
        :return: a list of all the series found in the database
        """
        series_names = self.session.query(Series).all()
        names = [series.name for series in series_names]
        for name in names:
            print(name)

    def get_all_unsnoozed_series(self):
        """
        :return: a list of all the series that are not snoozed
        """
        return self.session.query(Series).filter(Series.snoozed == 'False').all()

    def update_last_watched_episode(self, series_name, episode, season):
        """
        Updates the last watched episode for a certain tv series.
        :param series_name: the name of the tv series that is going to be updated
        :param episode: the number of the episode
        :param season: the number of the season
        :return: None
        """
        try:
            self.session.query(Series).filter(func.lower(Series.name) == series_name.lower()).update({
                Series.last_watched_episode: f"season{season} episode{episode}"}, synchronize_session=False)
            self.session.commit()
            print("Update done successfully!")
        except exc.SQLAlchemyError:
            self.session.rollback()
            raise Exception("Update failed.Rollback done!")

    def update_last_time_watched(self, series_name, date):
        """
         Updates the last watched date for a certain tv series.
        :param series_name: the name of the tv series that is going to be updated
        :param date: the last watched date
        :return: None
        """
        try:
            self.session.query(Series).filter(func.lower(Series.name) == series_name.lower()).update({
                Series.last_time_watched: date}, synchronize_session=False)
            self.session.commit()
            print("Update done successfully!")
        except exc.SQLAlchemyError:
            self.session.rollback()
            raise Exception("Update failed.Rollback done!")

    def update_rating(self, series_name, rating):
        """
        Updates the rating for a certain tv series.
        :param series_name: the name of the tv series that is going to be updated
        :param rating: the rating number
        :return: None
        """
        try:
            self.session.query(Series).filter(func.lower(Series.name) == series_name.lower()).update({
                Series.rating: rating}, synchronize_session=False)
            self.session.commit()
            print("Update done successfully!")
        except exc.SQLAlchemyError:
            self.session.rollback()
            raise Exception("Update failed.Rollback done!")

    def snooze_series(self, series_name):
        """
        Snoozes a series. Sets the snooze flag to TRUE.
        :param series_name: the name of the tv series that is going to be snoozed
        :return: None
        """
        try:
            self.session.query(Series).filter(func.lower(Series.name) == series_name.lower()).update({
                Series.snoozed: True}, synchronize_session=False)
            self.session.commit()
            print("Update done successfully!")
        except exc.SQLAlchemyError:
            self.session.rollback()
            raise Exception("Update failed.Rollback done!")

    def unsnooze_series(self, series_name):
        """
        Unsnoozes a series. Sets the snooze flag to FALSE.
        :param series_name: the name of the tv series that is going to be unsnoozed
        :return: None
        """
        try:
            self.session.query(Series).filter(func.lower(Series.name) == series_name.lower()).update({
                Series.snoozed: False}, synchronize_session=False)
            self.session.commit()
            print("Update done successfully!")
        except exc.SQLAlchemyError:
            self.session.rollback()
            raise Exception("Update failed.Rollback done!")

    def get_last_watched_episode(self, series_name):
        """
        :param series_name: the name of the tv series
        :return: the last seen episode of the given tv series
        """
        series_info = self.session.query(Series).filter(func.lower(Series.name) == series_name.lower()).one()
        if series_info.last_watched_episode is None:
            return "Looks like you haven't started the series yet!"
        else:
            last_watched_episode = str(series_info.last_watched_episode)
            return last_watched_episode

    def is_series_in_db(self, series_name):
        """
        :param series_name: the name of the tv series
        :return: a boolean value if the series is in the database or not
        """
        return self.session.query(Series).filter(func.lower(Series.name) == series_name.lower()).scalar() is not None

    def get_imdb_link(self, series_name):
        series_info = self.session.query(Series).filter(func.lower(Series.name) == series_name.lower()).one()

        return series_info.link_imdb


    # def get_movie_IMDb_ID(self, series_name):
    #     series_info = self.session.query(Series).filter(func.lower(Series.name) == series_name.lower()).one()
    #     return series_info.link_imdb[:]
