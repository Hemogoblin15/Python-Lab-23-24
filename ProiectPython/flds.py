from imdb import IMDb
from plyer import notification
import json


def get_series_episodes(series_title):
    ia = IMDb()

    # Search for the series by title
    search_results = ia.search_movie(series_title)
    seriesID = '0' + search_results[0].getID()
    episodes = ia.get_movie_episodes(int(seriesID))
    print (episodes)

    if search_results:
        # Get the first result (assuming it's the most relevant)
        series = search_results[0]

        # Retrieve episodes
        ia.update(series, episodes=True)

        episodes = series.data['episodes']

        return episodes
    else:
        return None


def get_saved_episodes(filename='saved_episodes.json'):
    try:
        with open(filename, 'r') as file:
            saved_episodes = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        saved_episodes = {}
    return saved_episodes


def save_episodes(filename='saved_episodes.json', episodes=None):
    with open(filename, 'w') as file:
        json.dump(episodes, file, indent=2)


def notify_new_episodes(series_title, filename='saved_episodes.json'):
    episodes = get_series_episodes(series_title)

    if episodes:
        saved_episodes = get_saved_episodes(filename)

        new_episodes = {}
        for season_num, season_episodes in episodes.items():
            if season_num not in saved_episodes:
                saved_episodes[season_num] = {}

            for episode_num, episode_title in season_episodes.items():
                if episode_num not in saved_episodes[season_num]:
                    saved_episodes[season_num][episode_num] = episode_title
                    new_episodes[season_num] = new_episodes.get(season_num, [])
                    new_episodes[season_num].append((episode_num, episode_title))

        if new_episodes:
            message = f"New episodes of '{series_title}':\n"
            for season_num, episodes_list in new_episodes.items():
                message += f"Season {season_num}:\n"
                for episode_num, episode_title in episodes_list:
                    message += f"  Episode {episode_num}: {episode_title}\n"

            # Use plyer to show a notification
            notification.notify(
                title=f"{series_title} New Episodes Notification",
                message=message,
                app_name='Series Notifier',
            )

            # Update saved episodes
            save_episodes(filename, saved_episodes)


if __name__ == "__main__":
    # Replace 'Breaking Bad' with the desired TV series title
    series_title = 'Breaking Bad'


    notify_new_episodes(series_title)
