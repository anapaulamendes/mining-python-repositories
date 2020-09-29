"""
Salva as informações de cada membro do repositório em members.json
"""
import csv
import json
import requests
from requests.auth import HTTPBasicAuth
from decouple import config

USERNAME = config('USERNAME')
PASSWORD = config('PASSWORD')

with open('../json/members.json') as f:
    members_dict = json.load(f)

for member in members_dict:
    response = requests.get(member['url'], auth=HTTPBasicAuth(USERNAME, PASSWORD))
    data = response.json()
    with open('../json/members/{}.json'.format(member['login']), 'w') as outfile:
        json.dump(data, outfile)
