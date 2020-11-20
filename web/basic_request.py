# -*- coding: utf-8 -*-

import os
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from fake_useragent import UserAgent

# define the path in which the file should be stored
path = Path(os.path.abspath(""))
data_path = path / "web/data"
# check if the directory exists
data_path.mkdir(parents=True, exist_ok=True)

# load the url from the .env file
env_path = data_path / ".env"
load_dotenv(dotenv_path=env_path, encoding="utf-8")
url = os.getenv("TUM_CALENDAR")

# define a fake useragent
ua = UserAgent()
headers = {
    "User-Agent": ua.random,
}
# define the parser to use
parser = "html5lib"

# create a session wich sends a get request
with requests.Session() as sess:
    res = sess.get(url=url, headers=headers)
    # save the website encoding
    encoding = res.encoding
# store the response in a BeautifulSoup object
html = BeautifulSoup(res.content, parser, from_encoding=encoding)
# save the content to a file
with open(data_path / "calendar.txt", mode="w", encoding=encoding) as file:
    file.write(html.text)
