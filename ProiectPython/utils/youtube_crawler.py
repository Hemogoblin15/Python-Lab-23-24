import json
import os.path
from selenium import webdriver
from selenium.webdriver.common.by import By


def write_to_json(query, titles, video_links):
    """
    Creates a json file to store the titles and videos of the YouTube uploads about an episode of a series.
    :param query: The query used to find said uploads.
    :param titles: The titles of the uploads.
    :param video_links: The links of the uploads.
    :return: None
    """
    data = {"query": query, "videos": []}

    for title, link in zip(titles, video_links):
        video_data = {"title": title, "link": link}
        data["videos"].append(video_data)

    json_directory = 'jsons'
    if not os.path.exists(json_directory):
        os.makedirs(json_directory)
    query = query.lower().replace(" ", "-")
    output_file = os.path.join(json_directory, f'{query}.json')
    with open(output_file, 'w') as json_file:
        json.dump(data, json_file, indent=2)


def try_get_youtube_uploads(driver, query, snoozy=1):
    uploads = ()
    for i in range(0, 10):
        uploads = get_youtube_uploads(driver, query, snoozy=1);
        if uploads is not None:
            return uploads
    return None


def get_youtube_uploads(driver, query, snoozy=1):
    # driver = webdriver.Firefox()
    """
    Crawls YouTube in order to find uploads about a series. Gets the series' name, a season of the series
    and an episode of that season as parameter.
    :param snoozy: flag to see if series is snoozed
    :param driver: the driver used for the web crawl
    :param query: The query needed to crawl YouTube. It contains the name of the series, a season number
    and an episode of that season.
    :return: The titles and links of the uploads it managed to find.
    """
    try:
        driver.get(f"https://www.youtube.com/results?search_query={query}&sp=CAI%253D")
        # TODO &sp=CAI%253D cod pentru filter by date
        driver.implicitly_wait(5)
        video_title_hrefs = []
        titles = []
        videos = driver.find_elements(By.ID, "video-title")
        for element in videos:
            href = element.get_attribute("href")
            if href:
                video_title_hrefs.append(href)
                titles.append(element.text)

        if snoozy == 1:
            write_to_json(query, titles[:10], video_title_hrefs[:10])
        return titles[:10], video_title_hrefs[:10]
    except Exception as e:
        print("error when scraping")
        print(e)
        return None

    # finally:
    #     driver.quit()
