import csv
from datetime import datetime

nome_arquivo = "cadastro.csv"

indice_desejado = int(input("Digite o índice do registro desejado (começando em 0): "))

def formatar_data_brasileira(data, formato_entrada="%m-%d-%Y", formato_saida="%d/%m/%Y"):
    data_obj = datetime.strptime(data, formato_entrada)
    return data_obj.strftime(formato_saida)

with open(nome_arquivo, mode='r') as arquivo_csv:
    leitor = csv.DictReader(arquivo_csv)
    
    for indice, linha in enumerate(leitor):
        if indice == indice_desejado:
            nome = linha["Nome"]
            data_nascimento = formatar_data_brasileira(linha["Data de Nascimento"])
            dia_cadastro = formatar_data_brasileira(linha["Dia do Cadastro"], formato_entrada="%Y-%m-%d")
            hora_cadastro = linha["Hora do Cadastro"]
            
            print(f"Registro {indice + 1}:")
            print(f"Nome: {nome}, Data de Nascimento: {data_nascimento}, Dia do Cadastro: {dia_cadastro}, Hora do Cadastro: {hora_cadastro}")
            break
    else:
        print(f"O registro com índice {indice_desejado} não foi encontrado.")
