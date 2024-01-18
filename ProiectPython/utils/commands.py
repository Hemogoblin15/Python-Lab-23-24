import os
from model.series import Series
from db_interaction.interaction import *
from datetime import datetime, date
from utils.youtube_crawler import get_youtube_uploads
import json


def add_series(repo):
    """
    This function calls the insert_series function from interaction.py to add a series to the database
    :param repo: the Interaction instance providing the gateway to the functions that address the database directly.
    :return: None
    """
    series_name = input("Insert the name of the series you want to add to the list: ")
    if not repo.is_series_in_db(series_name):
        season = input("Insert the number of the last season you watched and the episode number.\nSeason: ")
        episode = input("Episode: ")
        last_episode = f"season{season} episode{episode}"
        repo.insert_series(Series(series_name), last_episode)
    else:
        print("Series already present in the list.")
    return None


def remove_series(repo):
    """
    This function calls the delete_series function from interaction.py to remove a series from the database
    :param repo: the Interaction instance providing the gateway to the functions that address the database directly.
    :return: None
    """
    series_name = input("Enter the name of the series you'd wish to delete from the list: ")
    if not repo.is_series_in_db(series_name):
        print("Series not found in the list.")
    else:
        repo.delete_series(series_name)


def modify_series_rating(repo):
    """
    This function calls the update_rating function from interaction.py to update the rating of a series from the database
    :param repo: the Interaction instance providing the gateway to the functions that address the database directly.
    :return: None
    """

    series_name = input("Enter the name of the series you'd like to rate: ")
    if not repo.is_series_in_db(series_name):
        print("Series not found in the list.")
    else:
        rating = input("Enter the rating(1-10) you want to give this series: ")
        while float(rating) > 10.0 or float(rating) < 1:
            rating = input("Error! Please enter a rating from 1 to 10: ")
        repo.update_rating(series_name, rating)


def snooze_series(repo):
    """
    This function calls the snooze_series function from interaction.py to modify the snooze flag to true
    for a series in the database.
    :param repo: the Interaction instance providing the gateway to the functions that address the database directly.
    :return: None
    """
    series_name = input("Enter the name of the series you'd like to snooze: ")
    if not repo.is_series_in_db(series_name):
        print("Series not found in the list.")
    else:
        repo.snooze_series(series_name)


def unsnooze_series(repo):
    """
    This function calls the unsnooze_series function from interaction.py to modify the snooze flag to false
    for a series in the database.
    :param repo: the Interaction instance providing the gateway to the functions that address the database directly.
    :return: None
    """
    series_name = input("Enter the name of the series you'd like to unsnooze: ")
    if not repo.is_series_in_db(series_name):
        print("Series not found in the list.")
    else:
        repo.unsnooze_series(series_name)


def update_last_watched_episode(repo):
    """
    This function calls the update_last_watched_episode function from interaction.py to modify the last watched episode
    field  for a series in the database.
    :param repo: the Interaction instance providing the gateway to the functions that address the database directly.
    :return: None
    """
    series_name = input("Enter the name of the series you last watched: ")
    last_watched_season = input("Enter the number of the season and the episode you last watched. \nSeason: ")
    last_watched_episode = input("Episode: ")
    if not repo.is_series_in_db(series_name):
        print("Series not found in the list.")
    else:
        repo.update_last_watched_episode(series_name, last_watched_episode, last_watched_season)


def update_last_time_watched(repo):
    """
    This function calls the update_time_watched function from interaction.py to modify the last time the user watched
    a series in the database.
    :param repo: the Interaction instance providing the gateway to the functions that address the database directly.
    :return: None
    """
    series_name = input("Enter the name of the series you last watched: ")

    if not repo.is_series_in_db(series_name):
        print("Series not found in the list.")
    else:
        repo.update_last_time_watched(series_name, date.today())


def youtube_links(repo, driver):
    """
    This function provides the titles and links about a specific episode in a series in the database. This function only
    interacts with the database if the specified series is not found in the database, in which case it prompts the user
    to add it by calling the insert_series from interaction.py.
    :param repo: the Interaction instance providing the gateway to the functions that address the database directly.
    :return: the titles and links of the YouTube videos about an episode in a series in the database
    """
    series_name = input("Enter the name of the series you'd like to look up videos about: ")
    if not repo.is_series_in_db(series_name):
        series_add = input("The series is not on your list. Try to add it first!")
        return None

    uploads_subject = input("\nDo you wish to look up videos about the last episode you watched? Type yes or no. ")
    uploads_subject.lower()
    if uploads_subject == 'yes':
        last_episode = repo.get_last_watched_episode(series_name)
        search = series_name + " " + last_episode
        uploads = get_youtube_uploads(driver, search)
    else:
        season = input(f"Enter the number of the season of {series_name}: ")
        episode = input(f"And the episode number in season {season}: ")
        query = series_name + " " + f"season{season} " + f"episode{episode}"
        uploads = get_youtube_uploads(driver, query)
    return uploads


def get_imdb_link(repo):
    """
    This function provides the IMDb link of a series found in the database.
    :param repo: the Interaction instance providing the gateway to the functions that address the database directly.
    :return: the IMDb link of the series.
    """
    series_name = input("Enter the name of the series you'd like to get the IMDb link to: ")
    if not repo.is_series_in_db(series_name):
        print("Series not found in the list.")
    else:
        return repo.get_imdb_link(series_name)


def list_all_series(repo):
    """
    This function calls upon the get_all_series function to return all information about the series present in the
    database
    :param repo: the Interaction instance providing the gateway to the functions that address the database directly.
    :return: name, link_imdb, rating, last_episode_watched, last_time_watched, snoozed flag for every series in
    the database
    """
    return repo.get_all_series()


def format_scraped_data_to_dictionary(titles, video_links):
    videos = []
    for title, link in zip(titles, video_links):
        video_data = {"title": title, "link": link}
        videos.append(video_data)
    return videos


def json_snooze_notify(repo, driver):
    jsons = [file for file in os.listdir("jsons") if file.endswith('.json')]
    snooze_alert_jsons = []
    for files in jsons:
        no_extension = os.path.splitext(files)[0]
        snooze_alert_jsons.append(no_extension)

    series_names, last_episodes = repo.get_unsnoozed_series()
    unsnoozed_series = []
    for item1, item2 in zip(series_names, last_episodes):
        unsnoozed_series.append(
            f"{None if item1 is None else item1.replace(" ", "-")}-" + f"{None if item2 is None else item2.replace(" ", "-")}")

    for item in snooze_alert_jsons:
        if item in unsnoozed_series:
            json_conversion = f"./jsons/{item}.json"
            try:
                with open(json_conversion, 'r') as json_file:
                    data = json.load(json_file)
                    titles, links = get_youtube_uploads(driver, item.replace("-", " "))
                    new_data = format_scraped_data_to_dictionary(titles, links)

                    if data["videos"] != new_data:
                        notification.notify(
                            title='New uploads!',
                            message='There are new uploads on the episodes you looked up!',
                            app_icon=None,
                            timeout=5,
                        )
                        print("\nThese are the newest YouTube videos since your last search! Give them a look!")
                        for video in new_data:
                            if video not in data["videos"]:
                                print(f"{video['title']} {video['link']}")
                        print()
            except FileNotFoundError:
                print(f"The file '{json_conversion}' was not found.")
                return None


def command_picker(repo, driver):
    """
    The so-called menu of the application. Asks the user to pick a command to use. For each command, a
    function will be called upon to fulfill the required task.
    :param repo: the Interaction instance providing the gateway to the functions that address the database directly.
    :return: None
    """
    print("Welcome to your watchlist! What would you like to do next?\n"
          "1. Add series to the list.\n"
          "2. Remove series from the list.\n"
          "3. Rate a series.\n"
          "4. Snooze a series.\n"
          "5. Unsnooze a series.\n"
          "6. Update your last watched episode of a series.\n"
          "7. Update your last watch date of a series. \n"
          "8. Watch YouTube videos about a specific episode.\n"
          "9. Link to a series' IMDb page.\n"
          "10. List all series in the database\n"
          "11. Exit.\n")
    command = 0
    while command != '11':
        command = input("\nPick what you would like to do: ")
        if command == '11':
            break
        if command == '1':
            print("Adding series to the list.")
            add_series(repo)
        elif command == '2':
            print("Removing series from the list.")
            remove_series(repo)
        elif command == '3':
            print("Rating a series from the list.")
            modify_series_rating(repo)
        elif command == '4':
            print("Snoozing a series from the list.")
            snooze_series(repo)
        elif command == '5':
            print("Unsnoozing a series from the list.")
            unsnooze_series(repo)
        elif command == '6':
            print("Updating your last watched episode of this series.")
            update_last_watched_episode(repo)
        elif command == '7':
            print("Updating the last time you watched this series.")
            update_last_time_watched(repo)
        elif command == '8':
            print("You have chosen to see YouTube videos related to an episode.\n")
            titles, links = (youtube_links(repo, driver))
            print()
            if titles and links:
                for title, link in zip(titles, links):
                    print(f"Video title: {title}")
                    print(f"Video link: {link}")
        elif command == '9':
            print("Here is the link to this series' IMDb page.")
            print(get_imdb_link(repo))
        elif command == '10':
            print("Here are all the series in the list.")
            list_all_series(repo)
        else:
            print("Unknown command. Check the command list and take another try.")
