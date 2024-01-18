import requests
import time
from imdb import IMDb
from plyer import notification


def find_imdb_link(series_name):
    """
    Crawls IMDb searching for the IMDb page link of a specified series receiving its name as a parameter.
    :param series_name: The name of the series it needs to get the link of.
    :return: The link of the specified series or a string message in case it cannot find it.
    """
    ia = IMDb()
    results = ia.search_movie(series_name)
    if results:
        for series in results:
            imdb_link = ia.get_imdbURL(series)
            if series.data['title'].lower().replace(" ", "") == series_name.lower().replace(" ", ""):
                return imdb_link
        print("Could not find the series you asked for. Did you mean: ")
        for index, series in enumerate(results):
            print(f"{index + 1}. {series.data['title']}")

        print("\nType 0 if none of these apply.")
        choice = input("Choose one of these options: ")
        return ia.get_imdbURL(results[int(choice) - 1])
    else:
        return "Could not find the series."
