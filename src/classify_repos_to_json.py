"""
Classifica os repositórios em técnicos e não técnicos e salva no json: classified_repos.json
para ser usado como dicionário depois.
"""
import csv
import json

repos_info = []

with open('../csv/repositories_classified.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            line_count += 1
            repos_info.append({
                'name': row[1],
                'technical': row[0]
            })

with open('../json/classified_repos.json', 'w') as outfile:
    json.dump(repos_info, outfile)
