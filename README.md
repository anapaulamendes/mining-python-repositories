

# Mineração de Repositórios da Organização Python no Github


## Link para a organização do repositório:

https://github.com/python

## Definição:

- Analisar: o desenvolvimento de softwares da organização do Python no Github.
- Intuito: mensurar a contribuição técnica e não técnica de mulheres nos repositórios da organização Python no Github.
- Ponto de vista: pesquisador.
- Contexto: comunidade open source da linguagem de programação Python.


## Questões e Métricas:

 - Q1: Qual a porcentagem total de contribuições de mulheres nos repositórios da organização Python no Github sobre o total de contribuições?
 - Métrica: O número de commits feito por mulheres sobre o número de commits totais dos repositórios da organização do Python no Github.

- Q2: Qual a porcentagem de contribuições técnicas de mulheres nos repositórios da organização Python no Github sobre o total de contribuições?
- Métrica: O número de commits feitos por mulheres sobre o total de commits em repositórios técnicos da organização do Python no Github.

- Q3: Qual a porcentagem de contribuições não técnicas de mulheres nos repositórios da organização Python no Github sobre o total de contribuições?
- Métrica: O número de commits feitos por mulheres sobre o total de commits em repositórios não técnicos da organização do Python no Github.

- Q4: Quantas mulheres há na organização do Python no Github?
- Métrica: Número de mulheres na organização do Python no Github.

- Q5: Qual a porcentagem de contribuições técnicas de mulheres da organização nos repositórios da organização Python no Github sobre o total de contribuições?
- Métrica: O número de commits feitos por mulheres da organização sobre o total de commits em repositórios técnicos da organização do Python no Github.

- Q6: Qual a porcentagem de contribuições não técnicas de mulheres da organização nos repositórios da organização Python no Github sobre o total de contribuições?
- Métrica: O número de commits feitos por mulheres da organização sobre o total de commits em repositórios não técnicos da organização do Python no Github.

- Q7: Qual a porcentagem de contribuições técnicas de mulheres que não estão na organização nos repositórios da organização Python no Github sobre o total de contribuições?
- Métrica: O número de commits feitos por mulheres que não estão na organização sobre o total de commits em repositórios técnicos da organização do Python no Github.

- Q8: Qual a porcentagem de contribuições não técnicas de mulheres que não estão na organização nos repositórios da organização Python no Github sobre o total de contribuições?
- Métrica: O número de commits feitos por mulheres que não estão na organização sobre o total de commits em repositórios não técnicos da organização do Python no Github.


## Hipóteses:

- Nula: A contribuição de mulheres nos repositórios da organização Python é equivalente a contribuição de homens.
- Alternativa: A contribuição de mulheres nos repositórios da organização Python é diferente da contribuição de homens.


## Seleção de participantes:

Por conveniência. O grupo de participantes será composto de todos aqueles que tenham realizado qualquer tipo de atividade em pelo menos um dos repositórios da organização Python.


## Instalação:

Para instalar os pacotes necessários, execute:

```pip install -r requirements.txt```

## Uso:

Para construir os arquivos json que serão utilizados para as métricas, execute os seguintes scripts:

Entre na pasta de scripts:

`cd src`

*Minera todos os repositórios da organização Python e salva todos os commits, comments e issue_comments
nas pastas com os mesmos nomes, respectivamente.*
`python mine_repos.py`

*Salva as informações de cada membro do repositório em members.json.*
`python save_members_json.py`

*Salva as informações de cada repositório no csv: repositories.csv*
`python save_repo_info.py`

*Salva as informações de todos os membros do repositório através de uma raspagem por selenium*
`python scrape_members.py`

*Exibe o número de commits por repositório*
`python statistics_by_repo.py`

*Exibe algumas estatísticas sobre os membros do repositório e salva em json: classified_members
a classificação dos membros por gênero em json, para ser usado como dicionário depois.*
`python statistics_members.py`

*Salva todos os json de contribuidores de repositórios na pasta: contributors*
`python contributors_by_repo.py`

*Classifica os contribuidores de repositorios por gênero e salva no json: classified_contributors_commits.json
para uso em dicionário depois.*
`python classified_contributors.py`

*Classifica os membros do repositório por gênero e salva no csv: members.csv*
`python classify_members_to_csv.py`

*Classifica os repositórios em técnicos e não técnicos e salva no json: classified_repos.json
para ser usado como dicionário depois.*
`python classify_repos_to_json.py`

*Carrega para um json os contribuidores que não são da organização*
`python not_members_to_json.py`

*Responde as questões da pesquisa*
`python metrics.py`
