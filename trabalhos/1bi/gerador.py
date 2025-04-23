import pandas as pd

df = pd.read_csv('dados.csv')
x = df['dia nascimento'].mean()

# soma = df[
#     ('dia nascimento', [0])+
#     ('dia nascimento', [1])+
#     ('dia nascimento', [2])+
#     ('dia nascimento', [3])
# ]

# soma = df['dia nascimento'].iloc[0] + df['dia nascimento'].iloc[1] + df['dia nascimento'].iloc[2] + df['dia nascimento'].iloc[3]

# print(f'A soma das datas de nascimento e {soma}')

print(sum(x))