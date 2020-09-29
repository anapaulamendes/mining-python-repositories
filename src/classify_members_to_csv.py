"""
Classifica os membros do repositório por gênero e salva no csv: members.csv
"""
import nltk
import csv
import json
from nltk.corpus import names

female_names = names.words('female.txt')
male_names = names.words('male.txt')
neutral_names = [w for w in male_names if w in female_names]

with open('../json/members_scrape.json') as json_file:
    data = json.load(json_file)

with open('../csv/members.csv', mode='w') as members:
    members_info = csv.writer(members, delimiter=';')
    members_info.writerow(['name', 'user', 'gender'])
    for key, value in data.items():
        if value.split()[0] in neutral_names:
            gender = 'N'
        elif value.split()[0] in female_names:
            gender = 'F'
        elif value.split()[0] in male_names:
            gender = 'M'
        else:
            gender = 'not_identified'
        members_info.writerow([key, value, gender])
