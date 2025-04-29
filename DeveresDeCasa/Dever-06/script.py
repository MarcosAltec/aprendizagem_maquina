import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Carregar os dados Iris
iris = load_iris()
# print(f'iris{iris}')

X = iris.data
y = iris.target

# Dividir os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinar o modelo KNN
modelo = KNeighborsClassifier(n_neighbors=3)
print(f'modelo {modelo}')
modelo.fit(X_train, y_train)

# Solicitar entrada do usuário
print("Digite as medidas da flor (comprimento sépala, largura sépala, comprimento pétala, largura pétala), separados por espaço:")
entrada = [float(x) for x in input().split()]

print(f'numero{entrada}')

# Verificar se foram inseridos exatamente 4 valores
if len(entrada) != 4:
    print("Erro: Você precisa inserir **exatamente 4 valores**.")
else:
    entrada = np.array(entrada).reshape(1, -1)
    predicao = modelo.predict(entrada)
    print(f'predicao {predicao}')
    nome_flor = iris.target_names[predicao[0]]
    print(f'nome_flor {nome_flor}')

    print(f"A flor prevista é: {nome_flor}")
