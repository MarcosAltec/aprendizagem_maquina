import csv
from datetime import datetime

# Dados para as entradas
dados = [
    {"Nome": "Maria", "Data de Nascimento": "2000-01-15", "Dia do Cadastro": "2025-02-19", "Hora do Cadastro": "23:00"},
    {"Nome": "João", "Data de Nascimento": "1998-05-22", "Dia do Cadastro": "2025-02-19", "Hora do Cadastro": "23:01"},
    {"Nome": "Ana", "Data de Nascimento": "2001-11-30", "Dia do Cadastro": "2025-02-19", "Hora do Cadastro": "23:02"},
    {"Nome": "Pedro", "Data de Nascimento": "1999-07-10", "Dia do Cadastro": "2025-02-19", "Hora do Cadastro": "23:03"},
    {"Nome": "Clara", "Data de Nascimento": "2003-03-05", "Dia do Cadastro": "2025-02-19", "Hora do Cadastro": "23:04"},
]

# Nome do arquivo CSV
nome_arquivo = "cadastro.csv"

# Função para formatar as datas
def formatar_datas(dados):
    for entrada in dados:
        data_nascimento = datetime.strptime(entrada["Data de Nascimento"], "%Y-%m-%d")
        entrada["Data de Nascimento"] = data_nascimento.strftime("%m-%d-%Y")
        
        dia_cadastro = datetime.strptime(entrada["Dia do Cadastro"], "%Y-%m-%d")
        entrada["Dia do Cadastro"] = dia_cadastro.strftime("%Y-%m-%d")
    return dados

# Formatando as datas
dados_formatados = formatar_datas(dados)

# Escrevendo os dados no arquivo CSV
with open(nome_arquivo, mode='w', newline='') as arquivo_csv:
    colunas = ["Nome", "Data de Nascimento", "Dia do Cadastro", "Hora do Cadastro"]
    escritor = csv.DictWriter(arquivo_csv, fieldnames=colunas)
    
    # Escrever cabeçalho
    escritor.writeheader()
    
    # Escrever dados
    for entrada in dados_formatados:
        escritor.writerow(entrada)

print(f"Arquivo '{nome_arquivo}' criado com sucesso com datas formatadas!")
