"""
Exibe o número de commits por repositório
"""
import os
import json

all_files = os.listdir('../json/commits')
print(len(all_files))

repos_dict = {}

for file in all_files:
    with open('../json/commits/{}'.format(file)) as json_file:
        data = json.load(json_file)

    repos_dict[file] = []
    for d in data:
        for commit in d:
            repos_dict[file].append(commit)

for key, value in repos_dict.items():
    print(key, len(value))
