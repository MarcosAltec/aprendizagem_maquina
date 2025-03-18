import csv

nome_arquivo = "dados.csv"

lista_dados = []

with open(nome_arquivo, mode="r") as arquivo_csv:
    leitor = csv.DictReader(arquivo_csv)
    for linha in leitor:
        lista_dados.append({"Nome": linha["Nome"], "Idade": int(linha["Idade"])})