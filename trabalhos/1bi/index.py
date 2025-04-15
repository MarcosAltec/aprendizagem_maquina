import pandas as pd
import matplotlib.pyplot as plt
import os
import logging as log

log.basicConfig(
    filename="registros_de_log.log",
    level=log.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

log.info("Usuário iniciou o programa.")

while True: 
    caminho_arquivo = input("Digite o caminho do arquivo CSV ou JSON (ou 'S' para sair): ")

    if caminho_arquivo.lower() == "s":
        log.info("Usuário optou por sair do programa.")
        print("Saindo do programa...")
        exit()

    if os.path.exists(caminho_arquivo):
        if caminho_arquivo.endswith(".csv"):
            df = pd.read_csv(caminho_arquivo, encoding="utf-8")
            log.info(f"Arquivo CSV carregado com sucesso: {caminho_arquivo}")
        elif caminho_arquivo.endswith(".json"):
            df = pd.read_json(caminho_arquivo, encoding="utf-8")
            log.info(f"Arquivo JSON carregado com sucesso: {caminho_arquivo}")
        else:
            log.warning(f"Formato inválido fornecido: {caminho_arquivo}")
            print("Formato de arquivo inválido! Use CSV ou JSON")
            continue
        break
    else:
        log.error(f"Arquivo não encontrado: {caminho_arquivo}")
        print("Erro: O arquivo não foi encontrado! Verifique o caminho e tente novamente")

total_registros = df.shape[0]
quantidade_generos = df["genero"].value_counts()
registros_sem_educacao_pais = df["educacao_dos_pais"].isna().sum()

log.info(f"Total de registros carregados: {total_registros}")
log.info(f"Distribuição de gênero:\n{quantidade_generos.to_string()}")
log.info(f"Registros sem informação sobre educação dos pais: {registros_sem_educacao_pais}")

print("\nResumo dos dados carregados:")
print(f"- Total de registros: {total_registros}")
print(f"- Quantidades de homens e mulheres: \n{quantidade_generos.to_string()}")
print(f"- Registros sem informação sobre educação dos pais: {registros_sem_educacao_pais}")

df = df.dropna(subset=["educacao_dos_pais"])
log.info(f"Total de registros após remoção de valores vazios: {df.shape[0]}")

print(f"Total de registros após remoção de valores vazios: {df.shape[0]}")

mediana_attendance = df["attendance"].median()
df["attendance"] = df["attendance"].fillna(mediana_attendance)
log.info(f"Mediana de 'attendance': {mediana_attendance}")
log.info(f"Somatório da presença após ajuste: {df['attendance'].sum()}")

print(f"Mediana de 'attendance': {mediana_attendance}")
print(f"Somatório de presença após ajuste: {df['attendance'].sum()}")

colunas_numericas = df.select_dtypes(include=["number"]).columns.tolist()
colunas_numericas.remove("id")

while True:
    print("\nColunas disponíveis para análise:")
    for i, coluna in enumerate(colunas_numericas):
        print(f"{i + 1}. {coluna}")
    print("S. Sair")

    escolha = input("Escolha uma opção pelo número (ou 'S' para sair): ").strip()

    if escolha.lower() == "s":
        log.info("Usuário optou por sair da análise estatística.")
        print("Saindo do programa...")
        break

    if escolha.isdigit() and 1 <= int(escolha) <= len(colunas_numericas):
        coluna_escolhida = colunas_numericas[int(escolha) - 1]

        media = df[coluna_escolhida].mean()
        mediana = df[coluna_escolhida].median()
        moda = df[coluna_escolhida].mode()[0] if not df[coluna_escolhida].mode().empty else "Sem moda"
        desvio_padrao = df[coluna_escolhida].std()

        log.info(f"Estatísticas geradas para a coluna '{coluna_escolhida}': Média={media:.2f}, Mediana={mediana:.2f}, Moda={moda}, Desvio Padrão={desvio_padrao:.2f}")

        print(f"\nEstatísticas da coluna '{coluna_escolhida}':")
        print(f"- Média: {media:.2f}")
        print(f"- Mediana: {mediana:.2f}")
        print(f"- Moda: {moda}")
        print(f"- Desvio Padrão: {desvio_padrao:.2f}")
    else:
        log.warning("Usuário digitou uma opção inválida na análise estatística.")
        print("Opção inválida! Escolha um número da lista ou 'S' para sair.")

print("\nGerando gráficos...")
log.info("Iniciando geração de gráficos.")

# Gráfico de dispersão: Horas de Sono x Nota Final
plt.figure(figsize=(8, 5))
plt.scatter(df["horas_de_sono"], df["nota_final"], color='blue', alpha=0.6)
plt.xlabel("Horas de Sono")
plt.ylabel("Nota Final")
plt.title("Relação entre Horas de Sono e Nota Final")
plt.grid(True)
plt.show()
log.info("Gráfico de dispersão gerado: Horas de Sono x Nota Final.")

# Gráfico de barras: Idade x Média das Notas Intermediárias
media_notas_por_idade = df.groupby("idade")["midterm_Score"].mean()
plt.figure(figsize=(8, 5))
plt.bar(media_notas_por_idade.index, media_notas_por_idade.values, color="orange")
plt.xlabel("Idade")
plt.ylabel("Média das Notas Intermediárias")
plt.title("Idade x Média das Notas Intermediárias")
plt.show()
log.info("Gráfico de barras gerado: Idade x Média das Notas Intermediárias.")

# Gráfico de pizza: Distribuição das idades agrupadas
df["faixa_etaria"] = pd.cut(df["idade"], bins=[0, 17, 21, 24, 100], labels=["Até 17", "18 a 21", "21 a 24", "25 ou mais"])
faixas_etarias = df["faixa_etaria"].value_counts()

plt.figure(figsize=(7, 7))
plt.pie(faixas_etarias, labels=faixas_etarias.index, autopct="%1.1f%%", colors=["blue", "green", "red", "purple"])
plt.title("Distribuição das Idades (Agrupadas)")
plt.show()
log.info("Gráfico de pizza gerado: Distribuição das Idades Agrupadas.")

log.info("Execução do programa concluída com sucesso.")