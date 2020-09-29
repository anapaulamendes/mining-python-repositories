"""
Exibe algumas estatísticas sobre os membros do repositório e salva em json: classified_members
a classificação dos membros por gênero em json, para ser usado como dicionário depois.
"""
import csv
import json

woman = 0
man = 0
not_identified = 0

contributors_info = []

with open('../csv/members_manual_indentified.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            if row[2] == 'F':
                woman += 1
            elif row[2] == 'M':
                man += 1
            else:
                not_identified +=1
            line_count += 1

            contributors_info.append({
                'username': row[1],
                'name': row[0],
                'gender': row[2]
            })

with open('../json/classified_members.json', 'w') as outfile:
    json.dump(contributors_info, outfile)

total = woman + man + not_identified

mid_woman = (woman/total) * 100
mid_man = (man/total) * 100
mid_not_indentified = (not_identified/total) * 100

print("Total de mulheres: ", woman)
print("Total de homens: ", man)
print("Total de não indentificados: ", not_identified)
print("Quantidade de membros da organização: ", total)
print("Porcentagem de mulheres sobre o total: {}%".format(mid_woman))
print("Porcentagem de homens sobre o total: {}%".format(mid_man))
print("Porcentagem de gênero não indentificado: {}%".format(mid_not_indentified))
