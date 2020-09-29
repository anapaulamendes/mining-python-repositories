"""
Minera todos os repositórios da organização Python e salva todos os commits, comments e issue_comments
nas pastas com os mesmos nomes, respectivamente.
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
    commits_url = repo['commits_url'].split('{')[0]
    comments_url = repo['comments_url'].split('{')[0]
    issue_comment_url = repo['issue_comment_url'].split('{')[0]

    r = requests.get(commits_url, params=params, auth=HTTPBasicAuth(USERNAME, PASSWORD))
    link = r.headers.get('link', None)
    if link is not None:
        link_next = [l for l in link.split(',') if 'rel="last"' in l]
        if len(link_next) > 0:
            commits_url_pages = int(link_next[0][link_next[0].find("page=")+5:link_next[0].find("&")])
    else:
        commits_url_pages = 1

    r = requests.get(comments_url, params=params, auth=HTTPBasicAuth(USERNAME, PASSWORD))
    link = r.headers.get('link', None)
    if link is not None:
        link_next = [l for l in link.split(',') if 'rel="last"' in l]
        if len(link_next) > 0:
            comments_url_pages = int(link_next[0][link_next[0].find("page=")+5:link_next[0].find("&")])
    else:
        comments_url_pages = 1

    r = requests.get(issue_comment_url, params=params, auth=HTTPBasicAuth(USERNAME, PASSWORD))
    link = r.headers.get('link', None)
    if link is not None:
        link_next = [l for l in link.split(',') if 'rel="last"' in l]
        if len(link_next) > 0:
            issue_comment_url_pages = int(link_next[0][link_next[0].find("page=")+5:link_next[0].find("&")])
    else:
        issue_comment_url_pages = 1

    commits_url_results = []
    for page in range(1, commits_url_pages + 1):
        commits_url = repo['commits_url'].split('{')[0] + "?page={}&per_page=100".format(page)
        r = requests.get(commits_url, auth=HTTPBasicAuth(USERNAME, PASSWORD))
        response = json.loads(r.text)
        commits_url_results.append(response)

    with open('../json/commits/{}.json'.format(repo['name']), 'w') as outfile:
        json.dump(commits_url_results, outfile)

    comments_url_results = []
    for page in range(1, comments_url_pages + 1):
        comments_url = repo['comments_url'].split('{')[0] + "?page={}&per_page=100".format(page)
        r = requests.get(comments_url, auth=HTTPBasicAuth(USERNAME, PASSWORD))
        response = json.loads(r.text)
        comments_url_results.append(response)

    with open('../json/comments/{}.json'.format(repo['name']), 'w') as outfile:
        json.dump(comments_url_results, outfile)

    issue_comment_url_results = []
    for page in range(1, issue_comment_url_pages + 1):
        issue_comment_url = repo['issue_comment_url'].split('{')[0] + "?page={}&per_page=100".format(page)
        r = requests.get(issue_comment_url, auth=HTTPBasicAuth(USERNAME, PASSWORD))
        response = json.loads(r.text)
        issue_comment_url_results.append(response)

    with open('../json/issue_comments/{}.json'.format(repo['name']), 'w') as outfile:
        json.dump(issue_comment_url_results, outfile)

    print("{} - OK".format(repo['name']))
