"""
Salva as informações de todos os membros do repositório através de uma raspagem por selenium
"""
import csv
import json
import requests
from requests.auth import HTTPBasicAuth
from decouple import config
from selenium import webdriver

USERNAME = config('USERNAME')
PASSWORD = config('PASSWORD')

driver = webdriver.Chrome()

pages = ("https://github.com/orgs/python/people", "https://github.com/orgs/python/people?page=2",
        "https://github.com/orgs/python/people?page=3", "https://github.com/orgs/python/people?page=4")

users_info = {}

for page in pages:
    driver.get(page)
    list = driver.find_elements_by_class_name('table-list-item')
    for li in list:
        user = li.find_element_by_class_name('f5').text
        name = li.find_element_by_class_name('f4').text

        if user != "Follow":
            users_info[user] = name
        else:
            users_info[name] = name

print(len(users_info))

with open('../json/members_scrape.json', 'w') as outfile:
    json.dump(users_info, outfile)

for key, value in users_info.items():
    response = requests.get('https://api.github.com/users/{}'.format(key), auth=HTTPBasicAuth(USERNAME, PASSWORD))
    data = response.json()
    with open('../json/members_scrape/{}.json'.format(key), 'w') as outfile:
        json.dump(data, outfile)
