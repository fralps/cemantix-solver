# pylint: disable=W0603, W0622, W0621, C0103, C0301, R0801
"""Modules definitions"""
import os
import threading
import time
import datetime
from datetime import date
import json
from dotenv import load_dotenv
import requests
from requests.structures import CaseInsensitiveDict
import numpy as np

load_dotenv()

# ENV variables for Notion integration
CEMANTLE_NOTION_TOKEN = os.getenv("CEMANTLE_NOTION_TOKEN")
CEMANTLE_DATABASE_ID = os.getenv("CEMANTLE_DATABASE_ID")

# Prepare timer, words list, counter and threads exit event
start = time.time()
words = []
count = 0
exit_event = threading.Event()

# Parse the txt file,
# and store the words in a list
with open("dictionnaries/en/en_tiny_list.txt", encoding="utf-8") as file:
    line = file.readline()
    while line:
        line = file.readline()
        words.append(line.rstrip("\n"))

# Cemantle API URL
URL = "https://cemantle.certitudes.org/score"

# Headers definitions
headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/x-www-form-urlencoded"
headers["Host"] = "cemantle.certitudes.org"
headers["Origin"] = "https://cemantle.certitudes.org"
headers["referrer"] = "https://cemantle.certitudes.org/"
headers[
    "User-Agent"
] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"

# Run script and threads definitions
def main():
    """Normal threads"""
    threading.Thread(target=solve, args=[False, False]).start()
    threading.Thread(target=solve, args=[False, True]).start()
    threading.Thread(target=solve, args=[True, True]).start()

    # Random threads
    for i in range(25):
        print(f"Starting thread n°{i + 1}")
        threading.Thread(target=solve, args=[True, False]).start()


# Solve and find word of the day
def solve(random, reversed):
    """Take words from the list and randomize them with shuffle"""
    if random:
        list = np.array(words)
        np.random.shuffle(list)
    else:
        list = words

    if reversed:
        list = list[::-1]

    for word in list:
        data = f"word={word}".encode("utf-8")
        resp = requests.post(URL, headers=headers, data=data, timeout=30)
        score = resp.json()

        if "score" in score:
            print(f"\033[0;37m{word} ➡️ {score['score']}")
            global count
            count += 1
            if score["score"] == 1:
                end = time.time()
                os.system("clear")
                print(
                    f"\033[1;32mResult: {word} 🥳 in {str(datetime.timedelta(seconds = end - start))} after {count} attempts"
                )
                send_to_notion(
                    word, str(datetime.timedelta(seconds=end - start)), count
                )
                exit_event.set()
                break

            # Stopping remaining threads if the word is found
            if exit_event.is_set():
                break

# Send new word to Notion DB
def send_to_notion(word, time, count):
    """Request to Notion API"""
    api_endpoint = "https://api.notion.com/v1/pages"
    notion_headers = {
        "Authorization": f"Bearer {CEMANTLE_NOTION_TOKEN}",
        "Content-Type": "application/json",
        "Notion-Version": "2021-08-16",
    }
    timestamp = datetime.datetime.now()

    body = {
        "parent": {"database_id": f"{CEMANTLE_DATABASE_ID}"},
        "properties": {
            "Word": {
                "type": "rich_text",
                "rich_text": [{"type": "text", "text": {"content": word}}],
            },
            "Elapsed time": {
                "type": "rich_text",
                "rich_text": [{"type": "text", "text": {"content": time}}],
            },
            "Attempts": {"type": "number", "number": count},
            "Date": {
                "type": "rich_text",
                "rich_text": [
                    {
                        "type": "text",
                        "text": {"content": date.today().strftime("%d/%m/%Y")},
                    }
                ],
            },
            "Timestamp": {
                "type": "rich_text",
                "rich_text": [{"type": "text", "text": {"content": f"{timestamp}"}}],
            },
        },
    }

    response = requests.post(
        api_endpoint,
        data=json.dumps(body),
        headers=notion_headers,
        timeout=30
    )

    if response.status_code == 200:
        print("\033[1;32mNotion entry successfully created")


main()
