import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Ler os dados do arquivo CSV
dados = pd.read_csv("imc_dados.csv")

# Dividir os dados em variáveis independentes (X) e dependente (y)
X = dados[["IMC"]]  # Atributo de entrada
y = dados["Obeso"]  # Rótulo de saída

# Dividir os dados em conjuntos de treino e teste
X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.2, random_state=42)

# Criar e treinar o modelo de Regressão Logística
modelo = LogisticRegression()
modelo.fit(X_treino, y_treino)

print("Modelo treinado com sucesso!")
# Solicitar ao usuário um valor de IMC
imc_usuario = float(input("Digite o valor do IMC para verificar se é obeso: "))

# Fazer a previsão com base no modelo treinado
resultado = modelo.predict([[imc_usuario]])
probabilidade = modelo.predict_proba([[imc_usuario]])[0][1]

if resultado[0]:
    print(f"Com base no modelo, um IMC de {imc_usuario} é considerado **obeso** (Probabilidade: {probabilidade:.2f}).")
else:
    print(f"Com base no modelo, um IMC de {imc_usuario} **não é obeso** (Probabilidade: {probabilidade:.2f}).")