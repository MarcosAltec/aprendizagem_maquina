import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Students_Grading_Dataset.csv")

print(df.columns)
# print(df.head())

sns.set(style="whitegrid")

# 📊 **Gráfico de Dispersão (Scatter Plot) - relação entre notas finais e horas de estudo**
plt.figure(figsize=(8, 6))
sns.scatterplot(x=df["Study_Hours_per_Week"], y=df["Final_Score"], hue=df["Gender"])
plt.title("Relação entre Horas de Estudo e Nota Final")
plt.xlabel("Horas de Estudo")
plt.ylabel("Nota Final")
plt.show()

# 📈 **Gráfico de Barras - Média das notas por gênero**
plt.figure(figsize=(8, 6))
sns.barplot(x=df["Gender"], y=df["Final_Score"])
plt.title("Média das Notas por Gênero")
plt.xlabel("Gênero")
plt.ylabel("Nota Média")
plt.show()

# 📊 **Histograma - Distribuição das notas finais**
plt.figure(figsize=(8, 6))
sns.histplot(df["Final_Score"], bins=20, kde=True)
plt.title("Distribuição das Notas Finais")
plt.xlabel("Nota Final")
plt.ylabel("Frequência")
plt.show()

# 📊 **Box Plot - Comparação das Notas Finais por Nível de Educação dos Pais**
plt.figure(figsize=(8, 6))
sns.boxplot(x=df["Parent_Education_Level"], y=df["Final_Score"])
plt.title("Distribuição das Notas Finais por Nível de Educação dos Pais")
plt.xlabel("Nível de Educação dos Pais")
plt.ylabel("Nota Final")
plt.xticks(rotation=45)  # Rotaciona os rótulos para melhor visualização
plt.show()
