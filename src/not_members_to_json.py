import csv
import json

def load_json_to_dict(path):
    with open(path) as f:
        return json.load(f)

"""
Carrega membros classificados para um dicionário
Chaves: 'username', 'name', 'gender'
"""
classified_members = load_json_to_dict('../json/classified_members.json')

"""
Carrega contribuidores classificados para um dicionário
Chaves: 'username', 'name', 'gender'
"""
classified_contributors = load_json_to_dict('../json/classified_contributors.json')

contributors = []
members = []

for contributor in classified_contributors:
    contributors.append(contributor['username'])

for member in classified_members:
    members.append(member['username'])

classified_not_members = list(set(contributors) - set(members))

with open('../json/classified_not_members.json', 'w') as outfile:
    json.dump(classified_not_members, outfile)
