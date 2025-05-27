import seaborn as sns
from sklearn.preprocessing import LabelEncoder
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

df = sns.load_dataset('titanic')

# print(df)
print(f"O dataset tem {df.shape[0]} linhas e {df.shape[1]} colunas.")
print("1ª impressão", df.isnull().sum())

df['age'].fillna(df['age'].median(), inplace=True)
df['embarked'].fillna(df['embarked'].mode()[0], inplace=True)
df['embark_town'].fillna(df['embark_town'].mode()[0], inplace=True)
df.drop(columns=['deck', 'cabin'], inplace=True, errors='ignore')

print("2ª impressão\n", df.isnull().sum())

X = df.drop(columns=['survived'])  # Remove a coluna 'survived', pois é o alvo
y = df['survived']  # Define o target

# Criando o encoder
le = LabelEncoder()

X['sex'] = le.fit_transform(X['sex'])  # Converte 'male' e 'female' para 0 e 1
X = pd.get_dummies(X, columns=['embarked', 'class'], drop_first=True)
X.drop(columns=['alive', 'who', 'adult_male', 'embark_town', 'alone'], inplace=True, errors='ignore')

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Instanciar o modelo
model = LogisticRegression(max_iter=1000)  # Define um número maior de iterações para garantir convergência

# Treinar o modelo com os dados de treino
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# Calcular a acurácia
accuracy = accuracy_score(y_test, y_pred)
print(f"Acurácia do modelo: {accuracy:.2%}")