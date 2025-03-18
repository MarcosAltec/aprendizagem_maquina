import csv

# Passo 1: Criar o arquivo "dados.csv"
dados = [
    {"Nome": "Ana", "Idade": 25},
    {"Nome": "Bruno", "Idade": 30},
    {"Nome": "Carla", "Idade": 22},
    {"Nome": "Daniel", "Idade": 28},
    {"Nome": "Eduardo", "Idade": 35}
]

nome_arquivo = "dados.csv"

# Escrevendo os dados no arquivo CSV
with open(nome_arquivo, mode="w", newline="") as arquivo_csv:
    colunas = ["Nome", "Idade"]
    escritor = csv.DictWriter(arquivo_csv, fieldnames=colunas)
    escritor.writeheader()
    escritor.writerows(dados)

print(f"Arquivo '{nome_arquivo}' criado com sucesso!")

# Passo 2: Ler o arquivo "dados.csv" e armazenar os dados em uma lista
lista_dados = []

with open(nome_arquivo, mode="r") as arquivo_csv:
    leitor = csv.DictReader(arquivo_csv)
    for linha in leitor:
        lista_dados.append({"Nome": linha["Nome"], "Idade": int(linha["Idade"])})

# Pedir ao usuário para digitar um nome
nome_usuario = input("Digite o nome para buscar na lista: ")

# Verificar se o nome está na lista
encontrado = False
idade_maxima = max(pessoa["Idade"] for pessoa in lista_dados)  # Encontrar a maior idade

for pessoa in lista_dados:
    if pessoa["Nome"].lower() == nome_usuario.lower():
        encontrado = True
        idade = pessoa["Idade"]
        if idade == idade_maxima:
            print(f"{pessoa['Nome']} tem {idade} anos e é a pessoa mais velha da lista.")
        else:
            print(f"{pessoa['Nome']} tem {idade} anos e não é a pessoa mais velha da lista.")
        break

if not encontrado:
    print(f"O nome '{nome_usuario}' não foi encontrado na lista.")
