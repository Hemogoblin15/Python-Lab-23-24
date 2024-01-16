from model.series import Series
from db_interaction.interaction import *
from datetime import datetime, date
from utils.youtube_crawler import get_youtube_uploads

def add_series(repo):
    series_name = input("Insert the name of the series you want to add to the list: ")
    if not repo.is_series_in_db(series_name):
        repo.insert_series(Series(series_name))
    else:
        print("Series already present in the list.")
    return None


def remove_series(repo):
    series_name = input("Enter the name of the series you'd wish to delete from the list: ")
    if not repo.is_series_in_db(series_name):
        print("Series not found in the list.")
    else:
        repo.delete_series(series_name)


def modify_series_rating(repo):
    series_name = input("Enter the name of the series you'd like to rate: ")
    if not repo.is_series_in_db(series_name):
        print("Series not found in the list.")
    else:
        rating = input("Enter the rating(1-10) you want to give this series: ")
        while float(rating) > 10.0 or float(rating) < 1:
            rating = input("Error! Please enter a rating from 1 to 10: ")
        repo.update_rating(series_name, rating)


def snooze_series(repo):
    series_name = input("Enter the name of the series you'd like to snooze: ")
    if not repo.is_series_in_db(series_name):
        print("Series not found in the list.")
    else:
        repo.snooze_series(series_name)


def unsnooze_series(repo):
    series_name = input("Enter the name of the series you'd like to unsnooze: ")
    if not repo.is_series_in_db(series_name):
        print("Series not found in the list.")
    else:
        repo.unsnooze_series(series_name)


def update_last_watched_episode(repo):
    series_name = input("Enter the name of the series you last watched: ")
    last_watched_season = input("Enter the number of the season and the episode you last watched. \nSeason: ")
    last_watched_episode = input("Episode: ")
    if not repo.is_series_in_db(series_name):
        print("Series not found in the list.")
    else:
        repo.update_last_watched_episode(series_name, last_watched_episode, last_watched_season)


def update_last_time_watched(repo):
    series_name = input("Enter the name of the series you last watched: ")

    if not repo.is_series_in_db(series_name):
        print("Series not found in the list.")
    else:
        repo.update_last_time_watched(series_name, date.today())


def youtube_links(repo):
    series_name = input("Enter the name of the series you'd like to look up videos about: ")
    if not repo.is_series_in_db(series_name):
        series_add = input("The series is not on your list. Would you like to add it? Type yes or no: ")
        if series_add == 'yes':
            repo.insert_series(Series(series_name))
        else:
            return

    uploads_subject = input("\nDo you wish to look up videos about the last episode you watched? Type yes or no. ")
    uploads_subject.lower()
    if uploads_subject == 'yes':
        last_episode = repo.get_last_watched_episode(series_name).split(' ')[-1]
        search = series_name + " " + last_episode
        uploads = get_youtube_uploads(search)
    else:
        season = input(f"Enter the number of the season of {series_name}: ")
        episode = input(f"And the episode number in season {season}: ")
        query = series_name + " " + f"season {season} " + f"episode {episode}"
        uploads = get_youtube_uploads(query)
    return uploads


def get_imdb_link(repo):
    series_name = input("Enter the name of the series you'd like to get the IMDb link to: ")
    if not repo.is_series_in_db(series_name):
        print("Series not found in the list.")
    else:
        return repo.get_imdb_link(series_name)


def list_all_series(repo):
    return repo.get_all_series()


def command_picker(repo):
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
          "10. Exit.\n")
    command = 0
    while command != '10':
        command = input("\nPick what you would like to do: ")

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
            titles, links = (youtube_links(repo))
            print()
            if titles and links:
                for title, link in zip(titles, links):
                    print(f"Video title: {title}")
                    print(f"Video link: {link}")
                    print()
        elif command == '9':
            print("Here is the link to this series' IMDb page.")
            print(get_imdb_link(repo))
        else:
            print("Unknown command. Check the command list and take another try.")
