"""Fazer um exercício que leia o dicionário e efetue as seguintes alteracoes:

1 - Troque o nome completo do Estado pela sua respectiva sigla
2 - Sempre que houver um dado desconhecido trocar pela variável nula
3 - o email: acaso esteja como desconhecido trocar pelo modelo "nome.sobrenome@gmail.com", garantir que TODOS
OS EMAIL estejam em letra minúscula (low case)
4 - Trocar o nome do curso "A melhor linguagem do mundo" para "Python"
5 - Transformar o valor de cursos para o seguinte dicionário:
'cursos': {'Quantidade de cursos':
'Aluno Aplicado': True or False
'Aluno da melhor professora': True or False
'cursos do aluno': [lista dos cursos do aluno]}
O Aluno será aplicado se fizer mais de 2 cursos
O Aluno será aluno da melhor professora de estiver no curso de Python

*********************************************
Um exemplo de resolução:
['usuarios': [{'nome completo': 'Matheus Esteque',
'Estado': 'Roraima',
'email': 'Matheus.Esteque@gmail.com',
'cursos': ['Pascal', 'JavaScript', 'C', 'Assembly', 'C++', 'Rusty'],
'phone': 981972367,
'endereço': 'Estrada Girassol',
'CEP': 1549431}]

resposta esperada:
[{'nome completo': 'Matheus Esteque',
'Estado': 'RR',
'email': 'matheus.esteque@gmail.com',
'cursos': {'Quantidade de cursos': 6
'Aluno Aplicado': True
'Aluno da melhor professora': False
'cursos do aluno': ['Pascal', 'JavaScript', 'C', 'Assembly', 'C++', 'Rusty']},
'phone': 981972367,
'endereço': 'Estrada Girassol',
'CEP': 1549431}]
"""

exemplo = {'usuarios': [{'nome completo': 'Matheus Esteque',
                         'Estado': 'Roraima',
                         'email': 'Matheus.Esteque@gmail.com',
                         'cursos': ['Pascal', 'JavaScript', 'C', 'Assembly', 'C++', 'Rusty'],
                         'phone': 981972367,
                         'endereço': 'Estrada Girassol',
                         'CEP': 1549431}, ]}

sigla_estados = {'Roraima': 'RR',  # roubei colocando só os estados da lista? sim
                 'São Paulo': 'SP',
                 'Minas Gerais': 'MG',
                 'Alagoas': 'AL',
                 'Bahia': 'BA',
                 'Amapá': 'AP',
                 'Sergipe': 'SE',
                 'Mato Grosso do Sul': 'MS',
                 'Rio de Janeiro': 'RJ',
                 'Amazonas': 'AM',
                 'Paraíba': 'PB'}

# não vai estar tendo pep-8 pra essa linha aqui não, infelizmente:
response = {'usuarios': [{'nome completo': 'Matheus Esteque', 'Estado': 'Roraima', 'email': 'Matheus.Esteque@gmail.com', 'cursos': ['Pascal', 'JavaScript', 'C', 'Assembly', 'C++', 'Rusty'], 'phone': 981972367, 'endereço': 'Estrada Girassol', 'CEP': 1549431}, {'nome completo': 'Suellen Estevan', 'Estado': 'Rio de Janeiro', 'email': 'Suellen.Estevan@gmail.com', 'cursos': ['C', 'Go', 'Rusty', 'A melhor linguagem do mundo'], 'phone': 999614155, 'endereço': 'Rua Túlipa', 'CEP': 4800758}, {'nome completo': 'José da Silva', 'Estado': 'Bahia', 'email': 'José.da Silva@gmail.com', 'cursos': ['C#', 'Rusty', 'Ruby', 'Java', 'Pascal', 'Assembly', 'Go', 'JavaScript'], 'phone': 955203806, 'endereço': 'Avenida Alemanhã', 'CEP': 'desconhecido'}, {'nome completo': 'João Estevan', 'Estado': 'Minas Gerais', 'email': 'João.Estevan@gmail.com', 'cursos': ['A melhor linguagem do mundo'], 'phone': 928322023, 'endereço': 'desconhecido', 'CEP': 6434796}, {'nome completo': 'Matheus Barroso', 'Estado': 'Paraíba', 'email': 'desconhecido', 'cursos': ['C++', 'A melhor linguagem do mundo', 'Ruby', 'JavaScript', 'Pascal'], 'phone': 930388887, 'endereço': "Viela Joana d'Arc", 'CEP': 5800401}, {'nome completo': 'Suellen Barroso', 'Estado': 'Minas Gerais', 'email': 'Suellen.Barroso@gmail.com', 'cursos': ['Go', 'JavaScript', 'Java', 'Pascal'], 'phone': 975991061, 'endereço': 'Avenida Alemanhã', 'CEP': 'desconhecido'}, {'nome completo': 'Heleonor Falabella', 'Estado': 'Amazonas', 'email': 'Heleonor.Falabella@gmail.com', 'cursos': ['Go', 'Assembly', 'C', 'Java', 'Rusty', 'C++', 'C#', 'Ruby'], 'phone': 988951215, 'endereço': 'Viela Girassol', 'CEP': 3418991}, {'nome completo': 'José Neves', 'Estado': 'Paraíba', 'email': 'José.Neves@gmail.com', 'cursos': ['Pascal', 'Rusty', 'C#'], 'phone': 955926873, 'endereço': 'Viela Girassol', 'CEP': 7878593}, {'nome completo': 'José da Silva', 'Estado': 'Amazonas', 'email': 'José.da Silva@gmail.com', 'cursos': ['C', 'Ruby'], 'phone': 997945876, 'endereço': "Travessa Joana d'Arc", 'CEP': 9657827}, {'nome completo': 'Pedro Estevan', 'Estado': 'Rio de Janeiro', 'email': 'Pedro.Estevan@gmail.com', 'cursos': [], 'phone': 954132060, 'endereço': "Travessa Joana d'Arc", 'CEP': 3965367}, {'nome completo': 'João Teixeira', 'Estado': 'Minas Gerais', 'email': 'João.Teixeira@gmail.com', 'cursos': ['Java', 'C++', 'Ruby'], 'phone': 935369555, 'endereço': 'Viela Flores', 'CEP': 8059000}, {'nome completo': 'Regina Barroso', 'Estado': 'Paraíba', 'email': 'Regina.Barroso@gmail.com', 'cursos': ['Pascal', 'C', 'C++'], 'phone': 946610737, 'endereço': 'desconhecido', 'CEP': 'desconhecido'}, {'nome completo': 'Henrique Neves', 'Estado': 'Alagoas', 'email': 'Henrique.Neves@gmail.com', 'cursos': ['C#', 'C++', 'Assembly', 'Go'], 'phone': 992351215, 'endereço': 'Avenida Flores', 'CEP': 4708074}, {'nome completo': 'Kátia Teixeira', 'Estado': 'Bahia', 'email': 'Kátia.Teixeira@gmail.com', 'cursos': ['Go', 'A melhor linguagem do mundo', 'Assembly', 'Rusty'], 'phone': 954262905, 'endereço': 'Viela França', 'CEP': 4826598}, {'nome completo': 'Maria Torres', 'Estado': 'Bahia', 'email': 'Maria.Torres@gmail.com', 'cursos': ['JavaScript', 'Assembly', 'A melhor linguagem do mundo', 'Pascal'], 'phone': 913060348, 'endereço': 'Travessa Flores', 'CEP': 8064317}, {'nome completo': 'Eduardo Falabella', 'Estado': 'Amapá', 'email': 'desconhecido', 'cursos': ['C++', 'C', 'A melhor linguagem do mundo', 'JavaScript', 'Java', 'Ruby'], 'phone': 984532458, 'endereço': 'Rua Flores', 'CEP': 'desconhecido'}, {'nome completo': 'Pedro Neves', 'Estado': 'Rio de Janeiro', 'email': 'Pedro.Neves@gmail.com', 'cursos': ['C#'], 'phone': 922940639, 'endereço': "Avenida Joana d'Arc", 'CEP': 3579202}, {'nome completo': 'Vinícius Estevan', 'Estado': 'Rio de Janeiro', 'email': 'Vinícius.Estevan@gmail.com', 'cursos': ['C++', 'Java', 'JavaScript', 'Assembly', 'C'], 'phone': 983112802, 'endereço': 'Travessa Alemanhã', 'CEP': 1677359}, {'nome completo': 'Eduardo Esteque', 'Estado': 'Amazonas', 'email': 'Eduardo.Esteque@gmail.com', 'cursos': ['C', 'Java', 'C++', 'Go', 'Pascal', 'JavaScript', 'A melhor linguagem do mundo', 'C#'], 'phone': 912179028, 'endereço': 'Rua Girassol', 'CEP': 5508912}, {'nome completo': 'Regina da Silva', 'Estado': 'Amapá', 'email': 'Regina.da Silva@gmail.com', 'cursos': ['Assembly', 'JavaScript'], 'phone': 914656975, 'endereço': 'desconhecido', 'CEP': 8802034}, {'nome completo': 'Henrique Neves', 'Estado': 'Minas Gerais', 'email': 'desconhecido', 'cursos': ['Pascal', 'Go', 'C#', 'Ruby', 'JavaScript', 'C++'], 'phone': 993532734, 'endereço': "Estrada Joana d'Arc", 'CEP': 2717286}, {'nome completo': 'Heloísa Torres', 'Estado': 'Alagoas', 'email': 'desconhecido', 'cursos': ['Go', 'C++', 'A melhor linguagem do mundo'], 'phone': 948899759, 'endereço': 'Avenida Túlipa', 'CEP': 4827690}, {'nome completo': 'Heleonor Torres', 'Estado': 'Paraíba', 'email': 'Heleonor.Torres@gmail.com', 'cursos': ['A melhor linguagem do mundo', 'Go', 'Ruby'], 'phone': 952114194, 'endereço': 'Viela França', 'CEP': 'desconhecido'}, {'nome completo': 'Henrique Romano', 'Estado': 'Alagoas', 'email': 'Henrique.Romano@gmail.com', 'cursos': ['C', 'Assembly', 'Java', 'A melhor linguagem do mundo', 'C++', 'Rusty', 'JavaScript', 'C#'], 'phone': 922336239, 'endereço': "Estrada Joana d'Arc", 'CEP': 9710012}, {'nome completo': 'Maria Romano', 'Estado': 'Paraíba', 'email': 'Maria.Romano@gmail.com', 'cursos': ['JavaScript'], 'phone': 941444893, 'endereço': "Viela Joana d'Arc", 'CEP': 9077893}, {'nome completo': 'Maria Falabella', 'Estado': 'Amapá', 'email': 'Maria.Falabella@gmail.com', 'cursos': ['Rusty'], 'phone': 940735491, 'endereço': 'Rua Alemanhã', 'CEP': 9426658}, {'nome completo': 'José Falabella', 'Estado': 'Rio de Janeiro', 'email': 'José.Falabella@gmail.com', 'cursos': [], 'phone': 907509851, 'endereço': 'desconhecido', 'CEP': 'desconhecido'}, {'nome completo': 'José da Silva', 'Estado': 'Mato Grosso do Sul', 'email': 'José.da Silva@gmail.com', 'cursos': ['Assembly', 'C', 'Rusty', 'Java', 'JavaScript', 'C++'], 'phone': 925250696, 'endereço': 'Rua Alemanhã', 'CEP': 7661482}, {'nome completo': 'Heloísa Teixeira', 'Estado': 'Minas Gerais', 'email': 'Heloísa.Teixeira@gmail.com', 'cursos': ['Assembly', 'C', 'Java', 'Ruby'], 'phone': 977489770, 'endereço': 'Rua Flores', 'CEP': 'desconhecido'}, {'nome completo': 'Vinícius Esteque', 'Estado': 'São Paulo', 'email': 'Vinícius.Esteque@gmail.com', 'cursos': ['A melhor linguagem do mundo'], 'phone': 952919325, 'endereço': 'Travessa Girassol', 'CEP': 6487655}, {'nome completo': 'Maria Barroso', 'Estado': 'Roraima', 'email': 'Maria.Barroso@gmail.com', 'cursos': ['Ruby', 'Pascal', 'Go', 'C++', 'A melhor linguagem do mundo', 'Rusty'], 'phone': 924348753, 'endereço': 'desconhecido', 'CEP': 7992384}, {'nome completo': 'Heleonor Neves', 'Estado': 'Rio de Janeiro', 'email': 'Heleonor.Neves@gmail.com', 'cursos': ['JavaScript'], 'phone': 997233813, 'endereço': 'Estrada Girassol', 'CEP': 8454801}, {'nome completo': 'Heloísa Falabella', 'Estado': 'Mato Grosso do Sul', 'email': 'Heloísa.Falabella@gmail.com', 'cursos': ['Go', 'Assembly', 'JavaScript', 'Pascal'], 'phone': 964139926, 'endereço': 'Avenida França', 'CEP': 'desconhecido'}, {'nome completo': 'Matheus Teixeira', 'Estado': 'Amazonas', 'email': 'desconhecido', 'cursos': ['Go', 'A melhor linguagem do mundo', 'Assembly', 'Rusty', 'Java'], 'phone': 904741816, 'endereço': 'Viela Girassol', 'CEP': 7497763}, {'nome completo': 'Henrique Neves', 'Estado': 'São Paulo', 'email': 'Henrique.Neves@gmail.com', 'cursos': ['Assembly'], 'phone': 934810073, 'endereço': 'Travessa Girassol', 'CEP': 2734930}, {'nome completo': 'Henrique Esteque', 'Estado': 'Amazonas', 'email': 'Henrique.Esteque@gmail.com', 'cursos': ['Assembly', 'C#', 'Pascal'], 'phone': 979817437, 'endereço': 'Viela Túlipa', 'CEP': 'desconhecido'}, {'nome completo': 'Eduardo Estevan', 'Estado': 'Bahia', 'email': 'Eduardo.Estevan@gmail.com', 'cursos': [], 'phone': 922277672, 'endereço': 'Estrada Girassol', 'CEP': 8440323}, {'nome completo': 'Matheus Teixeira', 'Estado': 'Mato Grosso do Sul', 'email': 'Matheus.Teixeira@gmail.com', 'cursos': ['Go', 'JavaScript', 'Pascal', 'Rusty', 'Java'], 'phone': 998269572, 'endereço': 'Viela França', 'CEP': 3803095}, {'nome completo': 'Henrique Romano', 'Estado': 'São Paulo', 'email': 'Henrique.Romano@gmail.com', 'cursos': ['C++', 'A melhor linguagem do mundo', 'Java', 'Ruby', 'JavaScript'], 'phone': 998244096, 'endereço': 'Avenida Alemanhã', 'CEP': 4155188}, {'nome completo': 'Kátia da Silva', 'Estado': 'Roraima', 'email': 'Kátia.da Silva@gmail.com', 'cursos': ['C', 'Rusty', 'Assembly', 'Ruby', 'Java'], 'phone': 938840023, 'endereço': 'desconhecido', 'CEP': 2861813}, {'nome completo': 'Gabriel da Silva', 'Estado': 'Rio de Janeiro', 'email': 'Gabriel.da Silva@gmail.com', 'cursos': [], 'phone': 991783986, 'endereço': 'Estrada Alemanhã', 'CEP': 'desconhecido'}, {'nome completo': 'José Estevan', 'Estado': 'Minas Gerais', 'email': 'José.Estevan@gmail.com', 'cursos': ['Java', 'C', 'Assembly'], 'phone': 977508018, 'endereço': 'Viela Alemanhã', 'CEP': 8260941}, {'nome completo': 'Heloísa Falabella', 'Estado': 'Mato Grosso do Sul', 'email': 'desconhecido', 'cursos': ['JavaScript', 'Go', 'C++', 'Rusty'], 'phone': 984421256, 'endereço': 'Viela Girassol', 'CEP': 3524786}, {'nome completo': 'Pedro Torres', 'Estado': 'Alagoas', 'email': 'Pedro.Torres@gmail.com', 'cursos': ['A melhor linguagem do mundo'], 'phone': 956788326, 'endereço': 'Rua Flores', 'CEP': 9706924}, {'nome completo': 'Maria Falabella', 'Estado': 'Paraíba', 'email': 'Maria.Falabella@gmail.com', 'cursos': ['A melhor linguagem do mundo', 'C#', 'Go', 'Rusty', 'C'], 'phone': 947401473, 'endereço': "Rua Joana d'Arc", 'CEP': 'desconhecido'}, {'nome completo': 'Henrique da Silva', 'Estado': 'Bahia', 'email': 'desconhecido', 'cursos': ['JavaScript', 'Pascal', 'C++', 'A melhor linguagem do mundo', 'Ruby', 'Assembly', 'C', 'Rusty'], 'phone': 939060876, 'endereço': 'Travessa Alemanhã', 'CEP': 'desconhecido'}, {'nome completo': 'Regina Torres', 'Estado': 'Paraíba', 'email': 'Regina.Torres@gmail.com', 'cursos': ['C++', 'Rusty', 'A melhor linguagem do mundo', 'Go', 'Assembly', 'Pascal', 'C', 'C#'], 'phone': 955983777, 'endereço': "Avenida Joana d'Arc", 'CEP': 'desconhecido'}, {'nome completo': 'Kátia da Silva', 'Estado': 'Amapá', 'email': 'desconhecido', 'cursos': ['Ruby', 'Pascal', 'C', 'Java', 'C++'], 'phone': 954267455, 'endereço': 'Travessa Alemanhã', 'CEP': 3959388}, {'nome completo': 'Suellen Romano', 'Estado': 'Rio de Janeiro', 'email': 'Suellen.Romano@gmail.com', 'cursos': [], 'phone': 903839348, 'endereço': 'Estrada Flores', 'CEP': 3233684}, {'nome completo': 'Vinícius Estevan', 'Estado': 'Roraima', 'email': 'Vinícius.Estevan@gmail.com', 'cursos': [], 'phone': 959350072, 'endereço': 'Estrada Túlipa', 'CEP': 7298356}, {'nome completo': 'Maria Estevan', 'Estado': 'Amazonas', 'email': 'desconhecido', 'cursos': ['Pascal', 'Java', 'C', 'Rusty', 'Go'], 'phone': 905373043, 'endereço': 'Avenida Girassol', 'CEP': 5206744}, {'nome completo': 'Suellen Teixeira', 'Estado': 'Alagoas', 'email': 'Suellen.Teixeira@gmail.com', 'cursos': ['Rusty', 'JavaScript', 'Pascal', 'Ruby', 'C', 'A melhor linguagem do mundo', 'C++'], 'phone': 918221303, 'endereço': 'Travessa Alemanhã', 'CEP': 6866765}, {'nome completo': 'Vinícius Barroso', 'Estado': 'Sergipe', 'email': 'Vinícius.Barroso@gmail.com', 'cursos': ['Go', 'Ruby'], 'phone': 901010296, 'endereço': 'Viela Alemanhã', 'CEP': 'desconhecido'}, {'nome completo': 'Kátia Teixeira', 'Estado': 'São Paulo', 'email': 'Kátia.Teixeira@gmail.com', 'cursos': ['JavaScript', 'C++', 'A melhor linguagem do mundo'], 'phone': 942447760, 'endereço': 'Estrada Alemanhã', 'CEP': 1303953}, {'nome completo': 'Pedro Teixeira', 'Estado': 'Roraima', 'email': 'Pedro.Teixeira@gmail.com', 'cursos': ['Ruby', 'Go'], 'phone': 903691237, 'endereço': 'desconhecido', 'CEP': 8267810}, {'nome completo': 'Maria Neves', 'Estado': 'Minas Gerais', 'email': 'desconhecido', 'cursos': ['C', 'A melhor linguagem do mundo', 'Java', 'Assembly'], 'phone': 930951593, 'endereço': 'desconhecido', 'CEP': 'desconhecido'}, {'nome completo': 'Vinícius Teixeira', 'Estado': 'Paraíba', 'email': 'Vinícius.Teixeira@gmail.com', 'cursos': ['C#', 'Assembly', 'Ruby', 'Rusty', 'C++'], 'phone': 960062215, 'endereço': 'desconhecido', 'CEP': 1008666}, {'nome completo': 'Suellen Teixeira', 'Estado': 'São Paulo', 'email': 'desconhecido', 'cursos': ['C++', 'C', 'C#', 'Ruby', 'Go'], 'phone': 931762987, 'endereço': 'Avenida Alemanhã', 'CEP': 'desconhecido'}, {'nome completo': 'Heleonor Barroso', 'Estado': 'Mato Grosso do Sul', 'email': 'Heleonor.Barroso@gmail.com', 'cursos': ['JavaScript', 'Assembly', 'Go', 'A melhor linguagem do mundo', 'Ruby'], 'phone': 948131278, 'endereço': 'Viela Alemanhã', 'CEP': 4683786}, {'nome completo': 'Gabriel Teixeira', 'Estado': 'Minas Gerais', 'email': 'Gabriel.Teixeira@gmail.com', 'cursos': ['JavaScript', 'Ruby'], 'phone': 991999438, 'endereço': 'Avenida Alemanhã', 'CEP': 9049200}, {'nome completo': 'Henrique Romano', 'Estado': 'Paraíba', 'email': 'Henrique.Romano@gmail.com', 'cursos': [], 'phone': 993804994, 'endereço': 'desconhecido', 'CEP': 8661342}, {'nome completo': 'Heloísa da Silva', 'Estado': 'Roraima', 'email': 'Heloísa.da Silva@gmail.com', 'cursos': [], 'phone': 953375515, 'endereço': "Estrada Joana d'Arc", 'CEP': 2364058}, {'nome completo': 'Heloísa da Silva', 'Estado': 'Amazonas', 'email': 'Heloísa.da Silva@gmail.com', 'cursos': ['Go', 'Pascal', 'C++', 'Assembly'], 'phone': 923862744, 'endereço': 'Rua Flores', 'CEP': 3849516}, {'nome completo': 'João Falabella', 'Estado': 'Amazonas', 'email': 'desconhecido', 'cursos': ['C', 'Go'], 'phone': 956384979, 'endereço': "Viela Joana d'Arc", 'CEP': 7633798}, {'nome completo': 'Pedro Barroso', 'Estado': 'Minas Gerais', 'email': 'Pedro.Barroso@gmail.com', 'cursos': ['JavaScript'], 'phone': 935363984, 'endereço': 'desconhecido', 'CEP': 'desconhecido'}, {'nome completo': 'Matheus Neves', 'Estado': 'Amapá', 'email': 'Matheus.Neves@gmail.com', 'cursos': ['Assembly', 'JavaScript', 'Pascal', 'Java', 'Go'], 'phone': 907457018, 'endereço': 'Viela Túlipa', 'CEP': 'desconhecido'}, {'nome completo': 'José Romano', 'Estado': 'Paraíba', 'email': 'desconhecido', 'cursos': ['Ruby', 'Go'], 'phone': 983259311, 'endereço': 'desconhecido', 'CEP': 'desconhecido'}, {'nome completo': 'Pedro Estevan', 'Estado': 'Bahia', 'email': 'Pedro.Estevan@gmail.com', 'cursos': [], 'phone': 914525195, 'endereço': 'Viela Alemanhã', 'CEP': 'desconhecido'}, {'nome completo': 'Heleonor da Silva', 'Estado': 'Rio de Janeiro', 'email': 'Heleonor.da Silva@gmail.com', 'cursos': ['Java'], 'phone': 937027232, 'endereço': 'Estrada Túlipa', 'CEP': 9586146}, {'nome completo': 'José da Silva', 'Estado': 'Bahia', 'email': 'desconhecido', 'cursos': [], 'phone': 949153660, 'endereço': 'desconhecido', 'CEP': 2799111}, {'nome completo': 'João Falabella', 'Estado': 'Minas Gerais', 'email': 'João.Falabella@gmail.com', 'cursos': ['Ruby', 'Assembly', 'C#', 'C', 'A melhor linguagem do mundo', 'Java'], 'phone': 986964553, 'endereço': 'Travessa Girassol', 'CEP': 4424613}, {'nome completo': 'Kátia Estevan', 'Estado': 'Alagoas', 'email': 'Kátia.Estevan@gmail.com', 'cursos': ['Java', 'Assembly', 'C', 'C++'], 'phone': 989256588, 'endereço': 'Viela França', 'CEP': 5348484}, {'nome completo': 'Henrique Estevan', 'Estado': 'Amazonas', 'email': 'desconhecido', 'cursos': ['JavaScript', 'C++', 'Go', 'C'], 'phone': 940869642, 'endereço': 'Avenida Flores', 'CEP': 3252591}, {'nome completo': 'Matheus da Silva', 'Estado': 'Amazonas', 'email': 'desconhecido', 'cursos': ['C', 'Pascal', 'JavaScript', 'A melhor linguagem do mundo', 'Java', 'Ruby'], 'phone': 906776504, 'endereço': 'Travessa França', 'CEP': 'desconhecido'}, {'nome completo': 'Regina Esteque', 'Estado': 'Rio de Janeiro', 'email': 'Regina.Esteque@gmail.com', 'cursos': ['Ruby', 'A melhor linguagem do mundo', 'JavaScript', 'C', 'C++'], 'phone': 944286172, 'endereço': 'Avenida França', 'CEP': 1956258}, {'nome completo': 'Pedro Estevan', 'Estado': 'Amazonas', 'email': 'Pedro.Estevan@gmail.com', 'cursos': ['Rusty', 'C', 'C#'], 'phone': 933895494, 'endereço': 'Travessa Flores', 'CEP': 5933754}, {'nome completo': 'Maria Neves', 'Estado': 'Sergipe', 'email': 'desconhecido', 'cursos': ['JavaScript', 'Rusty'], 'phone': 926108939, 'endereço': "Rua Joana d'Arc", 'CEP': 8029010}, {'nome completo': 'João Barroso', 'Estado': 'Mato Grosso do Sul', 'email': 'João.Barroso@gmail.com', 'cursos': ['Go', 'Rusty', 'Pascal', 'C#', 'A melhor linguagem do mundo', 'Ruby', 'Assembly'], 'phone': 970604666, 'endereço': 'desconhecido', 'CEP': 'desconhecido'}, {'nome completo': 'Heloísa Esteque', 'Estado': 'Sergipe', 'email': 'Heloísa.Esteque@gmail.com', 'cursos': ['JavaScript', 'A melhor linguagem do mundo', 'Assembly', 'C#'], 'phone': 991611485, 'endereço': 'Rua Flores', 'CEP': 'desconhecido'}, {'nome completo': 'João Romano', 'Estado': 'Rio de Janeiro', 'email': 'João.Romano@gmail.com', 'cursos': ['Rusty', 'Java', 'JavaScript', 'Ruby'], 'phone': 911623802, 'endereço': 'Avenida França', 'CEP': 1357540}, {'nome completo': 'Eduardo da Silva', 'Estado': 'Amazonas', 'email': 'Eduardo.da Silva@gmail.com', 'cursos': ['C', 'C++', 'Java'], 'phone': 930336531, 'endereço': 'desconhecido', 'CEP': 'desconhecido'}, {'nome completo': 'Henrique Teixeira', 'Estado': 'Amazonas', 'email': 'Henrique.Teixeira@gmail.com', 'cursos': [], 'phone': 932231376, 'endereço': 'Estrada Alemanhã', 'CEP': 'desconhecido'}, {'nome completo': 'Suellen Romano', 'Estado': 'Rio de Janeiro', 'email': 'Suellen.Romano@gmail.com', 'cursos': ['Assembly', 'JavaScript'], 'phone': 935372754, 'endereço': 'Avenida França', 'CEP': 3968779}, {'nome completo': 'Gabriel Barroso', 'Estado': 'Alagoas', 'email': 'Gabriel.Barroso@gmail.com', 'cursos': ['Java'], 'phone': 964126728, 'endereço': 'Rua Girassol', 'CEP': 8467950}, {'nome completo': 'Heleonor da Silva', 'Estado': 'Amazonas', 'email': 'Heleonor.da Silva@gmail.com', 'cursos': ['JavaScript', 'Pascal', 'C#', 'Rusty', 'A melhor linguagem do mundo', 'Go', 'Assembly', 'C++'], 'phone': 939664838, 'endereço': 'Viela Girassol', 'CEP': 1945273}, {'nome completo': 'Gabriel Romano', 'Estado': 'Amapá', 'email': 'Gabriel.Romano@gmail.com', 'cursos': ['Ruby', 'Rusty', 'C++'], 'phone': 951332088, 'endereço': 'Estrada Túlipa', 'CEP': 4059679}, {'nome completo': 'José Neves', 'Estado': 'Alagoas', 'email': 'José.Neves@gmail.com', 'cursos': ['C++', 'Rusty', 'JavaScript', 'A melhor linguagem do mundo', 'C#', 'Java', 'C'], 'phone': 908889722, 'endereço': 'desconhecido', 'CEP': 'desconhecido'}, {'nome completo': 'Matheus da Silva', 'Estado': 'Sergipe', 'email': 'desconhecido', 'cursos': ['C', 'Pascal', 'JavaScript', 'C++'], 'phone': 967624373, 'endereço': 'Travessa França', 'CEP': 6391151}, {'nome completo': 'Maria Torres', 'Estado': 'Minas Gerais', 'email': 'Maria.Torres@gmail.com', 'cursos': [], 'phone': 917121500, 'endereço': "Rua Joana d'Arc", 'CEP': 1344812}, {'nome completo': 'Heleonor Esteque', 'Estado': 'Sergipe', 'email': 'Heleonor.Esteque@gmail.com', 'cursos': ['C#'], 'phone': 921639806, 'endereço': 'Rua Girassol', 'CEP': 3245380}]}


# Treinando a lógica do exercício com o exemplo fornecido: ***********************************

def exemplo_v1():
    """
    Fazendo uma função para fazer a resolução do exemplo, para depois poder
    iterar sobre o dicionário responses. A função pega o dicionário 'exemplos'
    e o conserta com as devidas orientações.
    :return: None
    """
    # checando se tem algum dado desconhecido:
    # print(exemplo['usuarios'][0]['nome completo'])  # como pegar um dado específico do usuário
    for k, v in exemplo['usuarios'][0].items():  # pra cada valor no dicionário de dados do usuário
        if v == 'desconhecido':
            exemplo['usuarios'][0][k] = None

    # colocando o email em letras minúsculas
    if exemplo['usuarios'][0]['email'] is None:
        exemplo['usuarios'][0]['email'] = \
            exemplo['usuarios'][0]['nome completo'].lower().replace(' ', '') + '@gmail.com'
    else:
        exemplo['usuarios'][0]['email'] = exemplo['usuarios'][0]['email'].lower()

    # trocando os nomes dos estados para suas siglas, que estão no dicionário siglas_estados
    for k, v in sigla_estados.items():  # percorre os pares de sigla_estados
        if exemplo['usuarios'][0]['Estado'] == k:  # se o estado for igual à chave (estado)
            exemplo['usuarios'][0]['Estado'] = v  # colocar o valor (sigla)

    # fazendo as modificações da chave 'cursos'
    # fazendo um dicionário novo pra colocar ele no lugar da lista que já temos
    cursos_novo = {'Quantidade de cursos': len(exemplo['usuarios'][0]['cursos']),
                   'Aluno Aplicado': None,
                   'Aluno da melhor professora': None,
                   'cursos do aluno': exemplo['usuarios'][0]['cursos'], }

    if cursos_novo['Quantidade de cursos'] > 2:  # condição para Aluno Aplicado
        cursos_novo['Aluno Aplicado'] = True
    else:
        cursos_novo['Aluno Aplicado'] = False

    for i, c in enumerate(cursos_novo['cursos do aluno']):  # condições sobre Python
        if c == 'A melhor linguagem do mundo':
            cursos_novo['cursos do aluno'][i] = 'Python'

        cursos_novo['Aluno da melhor professora'] = True if 'Python' in cursos_novo['cursos do aluno'] else False

    exemplo['usuarios'][0].update({'cursos': cursos_novo})  # colocando esse dicionário como valor da chave 'cursos'

    print(exemplo)


def oficial():
    """
    Agora vamos pegar o que fizemos e tentar iterar para o dicionário response.
    Não vou colocar os mesmos comentários, somente as linhas de código para ficar mais limpo;
    para ver a explicação da lógica por trás do código consultar a exemplo_v1().
    :return: None
    """


    """
    Antes eu estava fazendo apenas para o valor 0 da lista de usuários, agora vamos
    iterar sobre toda a lista, colocando um i onde tínhamos 0 e indo até
    o tamanho total dessa lista.
    """
    for i in range(len(response['usuarios'])):

        for k, v in response['usuarios'][i].items():
            if v == 'desconhecido':
                response['usuarios'][i][k] = None

        if response['usuarios'][i]['email'] is None:
            response['usuarios'][i]['email'] = \
                response['usuarios'][i]['nome completo'].lower().replace(' ', '') + '@gmail.com'
        else:
            response['usuarios'][i]['email'] = response['usuarios'][i]['email'].lower()

        for k, v in sigla_estados.items():
            if response['usuarios'][i]['Estado'] == k:
                response['usuarios'][i]['Estado'] = v

        cursos_novo = {'Quantidade de cursos': len(response['usuarios'][i]['cursos']),
                       'Aluno Aplicado': None,
                       'Aluno da melhor professora': None,
                       'cursos do aluno': response['usuarios'][i]['cursos'], }

        if cursos_novo['Quantidade de cursos'] > 2:  # condição para Aluno Aplicado
            cursos_novo['Aluno Aplicado'] = True
        else:
            cursos_novo['Aluno Aplicado'] = False

        for index, c in enumerate(cursos_novo['cursos do aluno']):  # condições sobre Python
            if c == 'A melhor linguagem do mundo':
                cursos_novo['cursos do aluno'][index] = 'Python'

            cursos_novo['Aluno da melhor professora'] = True if 'Python' in cursos_novo['cursos do aluno'] else False

        response['usuarios'][i].update({'cursos': cursos_novo})

    print(response)  # está printando na tela o resultado, se quiser ver de outro jeito modificar aqui!


def main():
    # exemplo_v1()  # função mais comentada e organizada para a resolução do exemplo
    oficial()  # só o código da iteração completa (sem comentários) pra poder ficar mais limpo


main()
