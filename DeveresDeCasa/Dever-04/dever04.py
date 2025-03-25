import random
import pandas as pd

# Crie a lista de frutas
frutas = ["maçã", "banana", "laranja", "uva", "maçã", "melão", "mamão", "banana"]

# Crie o arquivo "minhas_frutas.txt" e grave os dados
with open("minhas_frutas.txt", "w", encoding="latin1") as arquivo:
    arquivo.write("Fruta,Quantidade\n")  # Cabeçalho do arquivo
    for fruta in frutas:
        quantidade = random.randint(0, 100)  # Quantidade aleatória entre 0 e 100
        arquivo.write(f"{fruta},{quantidade}\n")  # Gravação no arquivo

print("Arquivo 'minhas_frutas.txt' criado com sucesso!")

# Ler o arquivo com a codificação correta
dados = pd.read_csv("minhas_frutas.txt", encoding="latin1")  # Lê o arquivo como DataFrame

# Somar as quantidades das frutas repetidas
dados_agrupados = dados.groupby("Fruta", as_index=False).sum()  # Agrupando por fruta e somando as quantidades

# Exibir o conteúdo no console como um DataFrame
print("\nConteúdo do arquivo agrupado por frutas:")
print(dados_agrupados)