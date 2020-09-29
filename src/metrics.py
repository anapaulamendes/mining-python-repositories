import os
import csv
import json

def all_files(path):
    return os.listdir(path)

def load_json_to_dict(path):
    with open(path) as f:
        return json.load(f)
"""
Carrega repositórios classificados para um dicionário
Chaves: 'name', 'technical'.
"""
classified_repos = load_json_to_dict('../json/classified_repos.json')

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

"""
Carrega contribuidores não membros para uma lista
"""
classified_not_members = load_json_to_dict('../json/classified_not_members.json')


"""
Q1)
Qual a porcentagem total de contribuições de mulheres nos repositórios da
organização Python no Github sobre o total de contribuições?
"""
woman_count = 0
man_count = 0
other_count = 0
contributors_files = all_files('../json/contributors')
for file in contributors_files:
    with open('../json/contributors/{}'.format(file)) as json_file:
        data = json.load(json_file)[0]
        for d in data:
            user = d['login']
            for contri in classified_contributors:
                if user in contri['username']:
                    gender = contri['gender']
            if gender == 'F':
                woman_count += d['contributions']
            elif gender == 'M':
                man_count += d['contributions']
            else:
                other_count += d['contributions']

total = woman_count + man_count + other_count

print("------------------------------ Q1 ------------------------------")
print("Qt de contribuições de mulheres: {}".format(woman_count))
print("Qt de contribuições de homens: {}".format(man_count))
print("Qt de contribuições de gênero não identificado: {}".format(other_count))
print("Porcentagem total de contribuições de mulheres: {}%".format((woman_count/total)*100))

"""
Q2)
Qual a porcentagem de contribuições técnicas de mulheres nos repositórios da
organização Python no Github sobre o total de contribuições?
"""
woman_count = 0
man_count = 0
other_count = 0
contributors_files = all_files('../json/contributors')
for file in contributors_files:
    for repo in classified_repos:
        if file.split('.')[0] == repo['name'] and repo['technical'] == 'True':
            with open('../json/contributors/{}'.format(file)) as json_file:
                data = json.load(json_file)[0]
                for d in data:
                    user = d['login']
                    for contri in classified_contributors:
                        if user in contri['username']:
                            gender = contri['gender']
                    if gender == 'F':
                        woman_count += d['contributions']
                    elif gender == 'M':
                        man_count += d['contributions']
                    else:
                        other_count += d['contributions']

total = woman_count + man_count + other_count

print("------------------------------ Q2 ------------------------------")
print("Qt de contribuições de mulheres: {}".format(woman_count))
print("Qt de contribuições de homens: {}".format(man_count))
print("Qt de contribuições de gênero não identificado: {}".format(other_count))
print("Porcentagem total de contribuições de mulheres: {}%".format((woman_count/total)*100))

"""
Q3)
Qual a porcentagem de contribuições não técnicas de mulheres nos repositórios da
organização Python no Github sobre o total de contribuições?
"""
woman_count = 0
man_count = 0
other_count = 0
contributors_files = all_files('../json/contributors')
for file in contributors_files:
    for repo in classified_repos:
        if file.split('.')[0] == repo['name'] and repo['technical'] == 'False':
            with open('../json/contributors/{}'.format(file)) as json_file:
                data = json.load(json_file)[0]
                for d in data:
                    user = d['login']
                    for contri in classified_contributors:
                        if user in contri['username']:
                            gender = contri['gender']
                    if gender == 'F':
                        woman_count += d['contributions']
                    elif gender == 'M':
                        man_count += d['contributions']
                    else:
                        other_count += d['contributions']

total = woman_count + man_count + other_count

print("------------------------------ Q3 ------------------------------")
print("Qt de contribuições de mulheres: {}".format(woman_count))
print("Qt de contribuições de homens: {}".format(man_count))
print("Qt de contribuições de gênero não identificado: {}".format(other_count))
print("Porcentagem total de contribuições de mulheres: {}%".format((woman_count/total)*100))

"""
Q4)
Quantas mulheres há na organização do Python no Github?
"""
woman = 0
man = 0
not_identified = 0

for member in classified_members:
    if member['gender'] == 'F':
        woman += 1
    elif member['gender'] == 'M':
        man += 1
    else:
        not_identified +=1

total = woman + man + not_identified
mid_woman = (woman/total) * 100
mid_man = (man/total) * 100
mid_not_indentified = (not_identified/total) * 100

print("------------------------------ Q4 ------------------------------")
print("Total de mulheres: ", woman)
print("Total de homens: ", man)
print("Total de gêneros não indentificados: ", not_identified)
print("Quantidade de membros da organização: ", total)
print("Porcentagem de mulheres sobre o total: {}%".format(mid_woman))
print("Porcentagem de homens sobre o total: {}%".format(mid_man))
print("Porcentagem de gênero não indentificado: {}%".format(mid_not_indentified))


"""
Q5)
Qual a porcentagem de contribuições técnicas de mulheres da
organização nos repositórios da organização Python no Github sobre o total de contribuições?
"""
woman_count = 0
man_count = 0
other_count = 0
contributors_files = all_files('../json/contributors')
for file in contributors_files:
    for repo in classified_repos:
        if file.split('.')[0] == repo['name'] and repo['technical'] == 'True':
            with open('../json/contributors/{}'.format(file)) as json_file:
                data = json.load(json_file)[0]
                for d in data:
                    user = d['login']
                    if user not in classified_not_members:
                        for contri in classified_members:
                            if user in contri['username']:
                                gender = contri['gender']
                        if gender == 'F':
                            woman_count += d['contributions']
                        elif gender == 'M':
                            man_count += d['contributions']
                        else:
                            other_count += d['contributions']

total = woman_count + man_count + other_count

print("------------------------------ Q5 ------------------------------")
print("Qt de contribuições de mulheres: {}".format(woman_count))
print("Qt de contribuições de homens: {}".format(man_count))
print("Qt de contribuições de gênero não identificado: {}".format(other_count))
print("Porcentagem total de contribuições de mulheres: {}%".format((woman_count/total)*100))

"""
Q6)
Qual a porcentagem de contribuições não técnicas de mulheres da organização nos repositórios
da organização Python no Github sobre o total de contribuições?
"""
woman_count = 0
man_count = 0
other_count = 0
contributors_files = all_files('../json/contributors')
for file in contributors_files:
    for repo in classified_repos:
        if file.split('.')[0] == repo['name'] and repo['technical'] == 'False':
            with open('../json/contributors/{}'.format(file)) as json_file:
                data = json.load(json_file)[0]
                for d in data:
                    user = d['login']
                    if user not in classified_not_members:
                        for contri in classified_members:
                            if user in contri['username']:
                                gender = contri['gender']
                        if gender == 'F':
                            woman_count += d['contributions']
                        elif gender == 'M':
                            man_count += d['contributions']
                        else:
                            other_count += d['contributions']

total = woman_count + man_count + other_count

print("------------------------------ Q6 ------------------------------")
print("Qt de contribuições de mulheres: {}".format(woman_count))
print("Qt de contribuições de homens: {}".format(man_count))
print("Qt de contribuições de gênero não identificado: {}".format(other_count))
print("Porcentagem total de contribuições de mulheres: {}%".format((woman_count/total)*100))

"""
Q7)
Qual a porcentagem de contribuições técnicas de mulheres que não estão na organização nos repositórios da
organização Python no Github sobre o total de contribuições?
"""
woman_count = 0
man_count = 0
other_count = 0
contributors_files = all_files('../json/contributors')
for file in contributors_files:
    for repo in classified_repos:
        if file.split('.')[0] == repo['name'] and repo['technical'] == 'True':
            with open('../json/contributors/{}'.format(file)) as json_file:
                data = json.load(json_file)[0]
                for d in data:
                    user = d['login']
                    if user in classified_not_members:
                        for contri in classified_contributors:
                            if user in contri['username']:
                                gender = contri['gender']
                        if gender == 'F':
                            woman_count += d['contributions']
                        elif gender == 'M':
                            man_count += d['contributions']
                        else:
                            other_count += d['contributions']

total = woman_count + man_count + other_count

print("------------------------------ Q7 ------------------------------")
print("Qt de contribuições de mulheres: {}".format(woman_count))
print("Qt de contribuições de homens: {}".format(man_count))
print("Qt de contribuições de gênero não identificado: {}".format(other_count))
print("Porcentagem total de contribuições de mulheres: {}%".format((woman_count/total)*100))

"""
Q8)
Qual a porcentagem de contribuições não técnicas de mulheres que não estão na organização nos repositórios da
organização Python no Github sobre o total de contribuições?
"""
woman_count = 0
man_count = 0
other_count = 0
contributors_files = all_files('../json/contributors')
for file in contributors_files:
    for repo in classified_repos:
        if file.split('.')[0] == repo['name'] and repo['technical'] == 'False':
            with open('../json/contributors/{}'.format(file)) as json_file:
                data = json.load(json_file)[0]
                for d in data:
                    user = d['login']
                    if user in classified_not_members:
                        for contri in classified_contributors:
                            if user in contri['username']:
                                gender = contri['gender']
                        if gender == 'F':
                            woman_count += d['contributions']
                        elif gender == 'M':
                            man_count += d['contributions']
                        else:
                            other_count += d['contributions']

total = woman_count + man_count + other_count

print("------------------------------ Q8 ------------------------------")
print("Qt de contribuições de mulheres: {}".format(woman_count))
print("Qt de contribuições de homens: {}".format(man_count))
print("Qt de contribuições de gênero não identificado: {}".format(other_count))
print("Porcentagem total de contribuições de mulheres: {}%".format((woman_count/total)*100))
