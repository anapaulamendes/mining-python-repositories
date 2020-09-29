"""
Classifica os contribuidores de repositorios por gênero e salva no json: classified_contributors_commits.json
para uso em dicionário depois.
"""
import os
import json
import nltk
import requests
from requests.auth import HTTPBasicAuth
from decouple import config
from nltk.corpus import names

USERNAME = config('USERNAME')
PASSWORD = config('PASSWORD')

female_names = names.words('female.txt')
male_names = names.words('male.txt')
neutral_names = [w for w in male_names if w in female_names]

all_files = os.listdir('../json/contributors')
print(len(all_files))

contributors_info = []

for file in all_files:
    with open('../json/contributors/{}'.format(file)) as json_file:
        data = json.load(json_file)[0]

    for contributor in data:
        r = requests.get(contributor['url'], auth=HTTPBasicAuth(USERNAME, PASSWORD))
        response = json.loads(r.text)
        if response['name']:
            name = response['name']
        else:
            name = response['login']
        if name.split()[0] in neutral_names:
            gender = 'N'
        elif name.split()[0] in female_names:
            gender = 'F'
        elif name.split()[0] in male_names:
            gender = 'M'
        else:
            gender = 'not_identified'

        contributors_info.append({
            'username': response['login'],
            'name': response['name'],
            'gender': gender
        })

with open('../json/classified_contributors.json', 'w') as outfile:
    json.dump(contributors_info, outfile)
