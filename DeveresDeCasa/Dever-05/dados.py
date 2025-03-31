import csv

# Criar o arquivo CSV com 10 entradas
dados = [
    {"IMC": 18.5, "Obeso": False},
    {"IMC": 22.0, "Obeso": False},
    {"IMC": 24.9, "Obeso": False},
    {"IMC": 25.1, "Obeso": True},
    {"IMC": 27.0, "Obeso": True},
    {"IMC": 30.5, "Obeso": True},
    {"IMC": 35.0, "Obeso": True},
    {"IMC": 40.2, "Obeso": True},
    {"IMC": 15.5, "Obeso": False},
    {"IMC": 29.9, "Obeso": True},
]

nome_arquivo = "imc_dados.csv"

with open(nome_arquivo, mode="w", newline="") as arquivo_csv:
    colunas = ["IMC", "Obeso"]
    escritor = csv.DictWriter(arquivo_csv, fieldnames=colunas)
    escritor.writeheader()
    escritor.writerows(dados)

print(f"Arquivo '{nome_arquivo}' criado com sucesso!")