import sys
import random

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    N = int(data[0])
    M = int(data[1])
    
    # Gerar palavras distintas
    min_distintas = M // 2
    # Criar lista de palavras distintas possíveis
    # Usaremos todas as letras minúsculas para formar palavras de 1 a 10 letras
    # Para garantir suficientes palavras distintas, geramos mais que min_distintas
    letras = 'abcdefghijklmnopqrstuvwxyz'
    palavras_distintas = set()
    
    # Gerar palavras aleatórias até ter pelo menos min_distintas
    while len(palavras_distintas) < min_distintas:
        tamanho = random.randint(1, 10)
        palavra = ''.join(random.choice(letras) for _ in range(tamanho))
        palavras_distintas.add(palavra)
    
    lista_distintas = list(palavras_distintas)
    
    # Número total de palavras na redação
    total_palavras = random.randint(N, M)
    
    # Quantas palavras distintas vamos usar (pelo menos min_distintas)
    # Mas não mais que o total de palavras
    usar_distintas = min(min_distintas, total_palavras)
    
    # Escolher palavras distintas aleatoriamente
    escolhidas_distintas = random.sample(lista_distintas, usar_distintas)
    
    # Completar o restante com repetições (pode incluir repetições das já escolhidas)
    redacao = escolhidas_distintas.copy()
    while len(redacao) < total_palavras:
        redacao.append(random.choice(escolhidas_distintas))
    
    # Embaralhar a ordem
    random.shuffle(redacao)
    
    # Imprimir
    print(' '.join(redacao))

if __name__ == "__main__":
    main()