# frase = "Este é um exemplo de codigo phyton"

# formatado = frase.split("e")

# print(formatado)

# setMeuConjunto = set()
# setMeuConjunto.add("a")
# setMeuConjunto.add('d')
# setMeuConjunto.add('b')
# setMeuConjunto.add(2)

# print(setMeuConjunto)

# lisMInhaLista = [56,1,2,5,4,'d','D', 5,2,1,5,2,4,56,4]

# print(lisMInhaLista)
# print(set(lisMInhaLista))

# f = open ("meuArquivo.txt","x")

# f = open ("meuArquivo.txt","a")

# f.write ("Minha primeira linha.")

# f.write ("Minha segunda linha.\nTerceira linha")

# f.close()

# f = open("meuArquivo.txt","r")

# arqMeuArquivo = f.read()

# print (arqMeuArquivo)

# f.close()

# a = 1

# b = 2

# c = 3

# print (a == b) #False

# print (a == b and a == a) #False

# print (a == b or a == a) #True

# print (a == a or a == a and a==c) #True

# print (a == a and a == a or a==c) #True

# print (a == a and a == c or a==a) #True

# print (a == c and (a == c or a==a)) #False

# lista1 = [1, 2, 3]

# lista2 = ['a', 'b', 'c']

# resultado = zip(lista1, lista2)

# for x, y in resultado:
#     print(f'Primeiro elemento: {x} e segundo: {y}')

# lstMinhaLista1 = [1,2,3,4,5]

# print (max(lstMinhaLista1))

# print (min(lstMinhaLista1))

# lstMinhaLista1 = ["1",2,3]

# print (1 in lstMinhaLista1)

# lstNumeros = [random.randint(1, 100) for _ in range(10)]

# import random

# # Criar uma lista com 10 números randômicos entre 1 e 100
# lista = [random.randint(1, 100) for _ in range(10)]

# # Encontrar o maior número na lista
# maior_numero = max(lista)

# print("Lista de números randômicos:", lista)
# print("Maior número:", maior_numero)

# import random

# # Criar uma lista com 10 números randômicos como strings
# lista = [str(random.randint(1, 100)) for _ in range(10)]

# # Encontrar o maior número na lista convertendo as strings de volta para inteiros
# maior_numero = max(lista, key=int)

# print("Lista de números randômicos como strings:", lista)
# print("Maior número (como string):", maior_numero)

# Criar uma lista fixa com caracteres numéricos
lista = ['10', 21, '42', 34, 93, '56', '3', 18, '57', '80']

# Converter os caracteres numéricos para inteiros
numeros = [int(item) for item in lista]

# Encontrar o maior número na lista
maior_numero = min(numeros)

print("Lista de números como strings:", lista)
print("Maior número:", maior_numero)
