import requests
from bs4 import BeautifulSoup
import html2text
import re
import json


def download_and_clean(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0"}
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract the main body content (remove scripts, styles, etc.)
        for script in soup(["script", "style", "img", "a"]):
            script.extract()

        body_text = soup.get_text()

        # Use html2text to convert HTML to clean text
        h = html2text.HTML2Text()
        h.ignore_links = True  # Ignore hyperlinks
        h.ignore_images = True  # Ignore images
        h.ignore_emphasis = True  # Ignore emphasis (italics, bold)
        h.ignore_tables = True  # Ignore tables
        clean_text = h.handle(body_text)
        clean_text = re.sub(r'[^\w\s\n<>/]+', '', clean_text)  # Removes special characters, except \n and <br>
        clean_text = re.sub(r'\s+', ' ', clean_text).strip()  # Removes extra whitespace and trims
        return clean_text

    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None


def url_list_downloader(url_list):
    for url in url_list:
        # Download and clean the text content from the current URL
        text = download_and_clean(url)
        # Check if text data was successfully obtained
        if text:
            # Open the local file in "append" mode
            with open("tempdir/temp_data.txt", "a") as myfile:
                # Convert the cleaned text (a dictionary) to a JSON string
                json_text = json.dumps(text)

                # Write the JSON string to the file
                myfile.write(json_text)
