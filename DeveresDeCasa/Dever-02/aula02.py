def solicitar_frase():
    while True:
        frase = input("Insira uma frase: ")
        if frase.strip():  # Verifica se a frase não está vazia ou só tem espaços
            return frase
        else:
            print("Entrada inválida. Por favor, insira uma frase.")

def analisar_frase(frase):
    num_caracteres = len(frase)
    palavras = frase.split()
    num_palavras = len(palavras)
    maior_palavra = max(palavras, key=len) if palavras else ""
    
    return num_caracteres, num_palavras, maior_palavra

def manipular_frase(frase):
    # Inversão por caracteres
    frase_invertida_chars = frase[::-1]
    
    # Inversão por palavras
    palavras = frase.split()
    frase_invertida_palavras = " ".join(palavras[::-1])
    
    # Alteração de caixa
    frase_maiusculas = frase.upper()
    frase_minusculas = frase.lower()
    
    # Tupla de palavras
    tupla_palavras = tuple(palavras)
    
    return frase_invertida_chars, frase_invertida_palavras, frase_maiusculas, frase_minusculas, tupla_palavras

def exibir_resultados(frase, num_caracteres, num_palavras, maior_palavra, frase_invertida_chars, frase_invertida_palavras, frase_maiusculas, frase_minusculas, tupla_palavras):
    print(f"\nResultados da Análise:\n")
    print(f"Número de caracteres: {num_caracteres}")
    print(f"Número de palavras: {num_palavras}")
    print(f"Maior palavra: {maior_palavra}")
    print(f"Frase invertida por caracteres: {frase_invertida_chars}")
    print(f"Frase invertida por palavras: {frase_invertida_palavras}")
    print(f"Frase em maiúsculas: {frase_maiusculas}")
    print(f"Frase em minúsculas: {frase_minusculas}")
    print(f"Tupla de palavras: {tupla_palavras}")

def main():
    frase = solicitar_frase()
    num_caracteres, num_palavras, maior_palavra = analisar_frase(frase)
    frase_invertida_chars, frase_invertida_palavras, frase_maiusculas, frase_minusculas, tupla_palavras = manipular_frase(frase)
    exibir_resultados(frase, num_caracteres, num_palavras, maior_palavra, frase_invertida_chars, frase_invertida_palavras, frase_maiusculas, frase_minusculas, tupla_palavras)

if __name__ == "__main__":
    main()
