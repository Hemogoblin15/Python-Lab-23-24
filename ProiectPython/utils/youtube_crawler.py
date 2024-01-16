import json
from selenium import webdriver
from selenium.webdriver.common.by import By


def write_to_json(query, titles, video_links):
    data = {"query": query, "videos": []}

    for title, link in zip(titles, video_links):
        video_data = {"title": title, "link": link}
        data["videos"].append(video_data)
    output_file = f'{query}.json'
    with open(output_file, 'w') as json_file:
        json.dump(data, json_file, indent=2)


def get_youtube_uploads(query):
    driver = webdriver.Firefox()

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
