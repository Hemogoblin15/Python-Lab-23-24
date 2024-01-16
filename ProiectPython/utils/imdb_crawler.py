import requests
import time
from imdb import IMDb
from plyer import notification


def find_imdb_link(series_title):
    ia = IMDb()
    results = ia.search_movie(series_title)
    if results:
        for movie in results:
            imdb_link = ia.get_imdbURL(movie)
            if movie.data['title'].lower().replace(" ", "") == series_title.lower().replace(" ", ""):
                return imdb_link
        print("Could not find the series you asked for. Did you mean: ")
        for index, movie in enumerate(results):
            print(f"{index + 1}. {movie.data['title']}")

        print("\nType 0 if none of these apply.")
        choice = input("Choose one of these options: ")
        return ia.get_imdbURL(results[int(choice) - 1])
    else:
        return "Could not find the series."

notification.notify(
    title='testing',
    message='message',
    app_icon=None,
    timeout=10,
)
