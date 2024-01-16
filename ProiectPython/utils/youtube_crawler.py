import json
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
    output_file = f'{query}.json'
    with open(output_file, 'w') as json_file:
        json.dump(data, json_file, indent=2)


def get_youtube_uploads(query):
    driver = webdriver.Firefox()
    """
    Crawls YouTube in order to find uploads about a series. Gets the series' name, a season of the series
    and an episode of that season as parameter.
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

        write_to_json(query, titles, video_title_hrefs)
        return titles, video_title_hrefs

    finally:
        driver.quit()


if __name__ == "__main__":
    search_query = 'fargo The castle clip'

    titles_list, href_list = get_youtube_uploads(search_query)

    if titles_list and href_list:
        for title, href in zip(titles_list, href_list):
            print(f"Video Title: {title}")
            print(f"Video Href: {href}")
            print()
    else:
        print("No videos found.")
