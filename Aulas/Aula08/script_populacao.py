import matplotlib.pyplot as plt

# Dados reais do crescimento populacional de Brasília (Ano e População)
anos = [2010, 2022, 2024]  # Anos disponíveis
populacao = [2570473, 2817381, 2982818]  # População estimada

# Criando o gráfico
plt.figure(figsize=(8, 5))
plt.plot(anos, populacao, marker='o', linestyle='-', color='b', label="População de Brasília")

# Personalizando o gráfico
plt.xlabel("Ano")
plt.ylabel("População")
plt.title("Crescimento Populacional de Brasília")
plt.legend()
plt.grid(True)

# Exibindo o gráfico
plt.show()
