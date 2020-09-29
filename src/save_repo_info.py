"""
Salva as informações de cada repositório no csv: repositories.csv
"""
import csv
import json

with open('../json/repos.json') as f:
    repos_dict = json.load(f)

with open('../csv/repositories.csv', mode='w') as repository:
    repo_info = csv.writer(repository, delimiter=';')
    repo_info.writerow(['name', 'description', 'url', 'contributors_url', 'commits_url',
                        'comments_url', 'issue_comment_url', 'language', 'forks_count',
                        'stargazers_count', 'archived'])
    for repo in repos_dict:
        repo_info.writerow([repo['name'], repo['description'], repo['url'], repo['contributors_url'],
                            repo['commits_url'], repo['comments_url'], repo['issue_comment_url'], repo['language'],
                            repo['forks_count'], repo['stargazers_count'], repo['archived']])
