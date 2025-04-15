import pandas as pd

# df = pd.DataFrame({'A': [1, 2, 2, 3, 3, 3],
#     'B': ['a', 'b', 'b', 'c', 'c', 'c']})
# print(df)
# df_result = df.drop_duplicates()
# print(df_result)

# meu_set = {1, 2, 3, 4, 4}  # Elementos duplicados são automaticamente removidos
# print(meu_set)

# meu_set.add(10)
# print(meu_set)  # {1, 2, 3, 4, 10}

# usuario1 = {"Inception", "Avatar", "Titanic", "Matrix"}
# usuario2 = {"Matrix", "Gladiador", "avatar", "Interestelar"}

# # Encontrar filmes assistidos por ambos (interseção)
# filmes_em_comum = usuario1 & usuario2
# print(filmes_em_comum)  # Saída: {'Matrix', 'Avatar'}

# lista = [10, 20, 30, 40, 50]
# for i in range(len(lista)):
#     if lista[i] > 25:
#         print(lista[i])

# frase = "Python é uma linguagem poderosa"
# palavras = frase.split()
# nova_frase = " ".join(palavras[::-1])
# print(nova_frase)

# import pandas as pd
# data = {'Nome': ['Alice', 'Bob', 'Charlie'],
# 'Idade': [25, 30, 28],
# 'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte']}
# df = pd.DataFrame(data)
# print(df)

# import pandas as pd
# # Criando um arquivo CSV de exemplo (você pode substituir pelo seu arquivo)
# data = {'Nome': ['Alice', 'Bob', 'Charlie', 'David', 'Emily', 'Fernando'],
# 'Idade': [25, 30, 28, 22, 35, 29],
# 'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Salvador',
# 'Brasília', 'Curitiba']}
# df = pd.DataFrame(data)
# # df.to_csv('clientes.csv', index=False)
# # Ler o arquivo CSV para um DataFrame
# df_clientes = pd.read_csv('clientes.csv')
# # Imprimir as 5 primeiras linhas
# print(df_clientes.head())
# # Calcular a média da idade
# media_idade = df_clientes['Idade'].mean()
# print(f"\nMédia da idade dos clientes: {media_idade}")

# data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
# df = pd.DataFrame(data)
# print(df.loc[1]['B'])

# strFrase = "Python eh top"
# print(strFrase[1:4:2])

# df = pd.read_csv('dados3.csv')
# df.dropna(inplace=True)
# print(len(df))

# lista = [1, 2, 2, 3, 4, 4, 5]
# print(set(lista))

# df = pd.DataFrame({'col1': [1, None, 3], 'col2': [None, 5, 6]})
# df['col1'].fillna(0, inplace=True)
# print(df['col1'].tolist())

# lisMinhaLista = [1,1,1,1,2,2,21,3,4,51,23,1,2,3,5,8] 
# lisMinhaLista.append(18)
# print (set(lisMinhaLista))

# lstMinhaLista = [1,2,3,4,5]
# x = 1
# y = 1
# for qlqNome in lstMinhaLista:
#     x += 1
#     print(x)
# y += 2

# lstMinhaLista1 = [1,2,3]
# lstMinhaLista2 = ['a','b','c']
# lstMinhaLista3 = [100,200,300]
# lstMinhaLista4 = list(zip(lstMinhaLista1,lstMinhaLista2,lstMinhaLista3))
# print (lstMinhaLista4)

# srtMinhaString = 'O IESB tem o melhor curso de ADS do Brasil.'
# lisMinhaLista = srtMinhaString.split()
# lisMinhaLista2 = lisMinhaLista[-3:]
# strMinhaString2 = lisMinhaLista2[0] + ' ' + lisMinhaLista2[1] + ' ' + lisMinhaLista2[2]
# print (f'O {lisMinhaLista[1]} é O {lisMinhaLista[4]} em {strMinhaString2}')

a = [1, 7, 2]
myvar = pd.Series(a, index = ["a", "b", "c"])
print(myvar, "aaaa")
print(myvar['b'], "bbbb")