import sys

def main():
    # Lê toda a entrada de uma vez para eficiência
    data = sys.stdin.read().split()
    
    # Verifica se há dados suficientes (embora o problema garanta o formato)
    if len(data) < 12:
        return

    # Converte os primeiros 6 números para inteiros (Aposta)
    # Converte os próximos 6 números para inteiros (Sorteio)
    # Usamos set para facilitar a contagem de interseção
    bet_numbers = set(map(int, data[:6]))
    drawn_numbers = set(map(int, data[6:12]))
    
    # Calcula quantos números foram acertados
    hits = len(bet_numbers.intersection(drawn_numbers))
    
    # Determina o prêmio baseado na quantidade de acertos
    if hits == 6:
        print("sena")
    elif hits == 5:
        print("quina")
    elif hits == 4:
        print("quadra")
    elif hits == 3:
        print("terno")
    else:
        print("azar")

if __name__ == "__main__":
    main()