"""
Salva todos os json de contribuidores de repositórios na pasta: contributors
"""
import json
import requests
from requests.auth import HTTPBasicAuth
from decouple import config

USERNAME = config('USERNAME')
PASSWORD = config('PASSWORD')
params = {'page': 1, 'per_page':100}

with open('../json/repos.json') as json_file:
    data = json.load(json_file)

for repo in data:
    print(repo['name'])
    contributors_url = repo['contributors_url']

    r = requests.get(contributors_url, params=params, auth=HTTPBasicAuth(USERNAME, PASSWORD))
    link = r.headers.get('link', None)
    if link is not None:
        link_next = [l for l in link.split(',') if 'rel="last"' in l]
        if len(link_next) > 0:
            contributors_url_pages = int(link_next[0][link_next[0].find("page=")+5:link_next[0].find("&")])
    else:
        contributors_url_pages = 1

    contributors_url_results = []
    for page in range(1, contributors_url_pages + 1):
        contributors_url = repo['contributors_url'].split('{')[0] + "?page={}&per_page=100".format(page)
        r = requests.get(contributors_url, auth=HTTPBasicAuth(USERNAME, PASSWORD))
        if r.text:
            response = json.loads(r.text)
        else:
            response = {}
        contributors_url_results.append(response)

    with open('../json/contributors/{}.json'.format(repo['name']), 'w') as outfile:
        json.dump(contributors_url_results, outfile)
