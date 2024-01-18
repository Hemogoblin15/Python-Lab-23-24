from model.series import Series
from sqlalchemy import exc, func
from utils.imdb_crawler import find_imdb_link
import datetime
from plyer import notification


class Interaction:
    """
    This class provides a "bridge" between the database and the python code. Its purpose
        is to make a gateway for solving the queries.

    Attributes

    session:
        session object that provides support for the queries directed towards the database

    Functions

    insert_series(series):
        Adds a new TV series to the database.
    delete_series(series_name):
        Deletes a TV series from the database.
    get_all_series():
        Returns a list of all the series present in the series list provided by the database
    update_last_watched_episode(series_name, episode, season):
        Updates the last watched episode for a TV series.
    update_last_watched_date(series_name, date):
        Updates the last date a TV series was watched.
    update_rating(series_name, rating):
        Updates the user rating for a TV series.
    snooze_series(series_name):
        Sets the TV series' snooze flag in the database to true.
    unsnooze_series(series_name):
        Sets the TV series' snooze flag in the database to false.
    get_last_seen_episode(series_name):
        Returns the last seen episode for a series.
    is_series_in_db(series_name):
        Tests whether the series with the specified series name exists in the database
    """

    def __init__(self, session):
        """
        Constructor.
        :param session:
            creating a session to interact with the database for the purpose of solving queries
        """
        self.session = session

    def insert_series(self, series: Series, last_episode):
        """
        Inserts new TV series to the database.
        :param series: a TV series object that will be added to the database.
        :param last_episode: prompt the user to insert the last episode they watched.
        :return: None
        """
        series.link_imdb = find_imdb_link(series.name)
        series.last_watched_episode = last_episode
        try:
            self.session.add(series)
            self.session.commit()
            print(f'series added successfully.')
        except exc.SQLAlchemyError:
            self.session.rollback()
            raise Exception("Could not add series. Rollback done.")

    def delete_series(self, series_name):
        """
        Deletes a TV series from the database.
        :param series_name: takes the name of the series the user wants to delete from the table
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
        This function has the purpose to print every series found in the database.
        :return: returns all the series in the database table. getter for every item present in the list
        """
        series = self.session.query(Series).all()
        for show in series:
            print(f"\n{show.name}, imdb_link: {show.link_imdb}, rating: {show.rating}, "
                  f"last watched episode: {show.last_watched_episode}, last time watched: {show.last_time_watched}, snoozed: {show.snoozed}")

    def get_unsnoozed_series(self):
        """
        This function has the purpose of returning every series in the database with the snoozed flag set to false.
        :return: returns all the series in the database with the snoozed flag set to false
        """
        series = self.session.query(Series).filter(Series.snoozed == False).all()
        series_names = []
        last_episodes = []
        for show in series:
            series_names.append(show.name)
            last_episodes.append(show.last_watched_episode)
        return series_names, last_episodes

    def update_last_watched_episode(self, series_name, episode, season):
        """
        Updates the last watched episode for the TV series.
        :param series_name: name of the TV series whose last_watched episode will be updated
        :param episode: episode number
        :param season: season number
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
         Updates the last watched date for a TV series to today's date.
        :param series_name: name of the TV series whose last_time_watched will be updated
        :param date: takes today's date
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
        Updates the rating for a TV series.
        :param series_name: the name of the TV series whose rating is to be updated
        :param rating: takes a number of the user's choosing
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
        :param series_name: the TV series that was chosen to be snoozed
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
        :param series_name: the TV series that was chosen to be unsnoozed
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
        :param series_name: the name of the TV series
        :return: returns the last episode of that series the user watched
        """
        series_info = self.session.query(Series).filter(func.lower(Series.name) == series_name.lower()).one()
        if series_info.last_watched_episode is None:
            print ("Looks like you haven't started watching this series yet!")
            return str(series_info.name)
        else:
            last_watched_episode = str(series_info.last_watched_episode)
            return last_watched_episode

    def is_series_in_db(self, series_name):
        """
        :param series_name: the name of the TV series
        :return: returns whether the series asked for is present in the database. returns a boolean
        """
        return self.session.query(Series).filter(func.lower(Series.name) == series_name.lower()).scalar() is not None

    def get_imdb_link(self, series_name):
        series_info = self.session.query(Series).filter(func.lower(Series.name) == series_name.lower()).one()

        return series_info.link_imdb

    # def get_series_IMDb_ID(self, series_name):
    #     series_info = self.session.query(Series).filter(func.lower(Series.name) == series_name.lower()).one()
    #     return series_info.link_imdb[:]
