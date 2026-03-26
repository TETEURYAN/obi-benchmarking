import sys

def main():
    # Leitura rápida da entrada
    data = sys.stdin.read().split()
    
    if not data:
        return

    # H: Heli, P: Policia, F: Fugitivo, D: Direção
    H = int(data[0])
    P = int(data[1])
    F = int(data[2])
    D = int(data[3])

    # Posição atual começa onde o fugitivo está
    atual = F

    # Simula o movimento passo a passo
    # Como o problema garante que H, P e F são distintos, o loop terminará
    # quando encontrarmos H ou P.
    while True:
        # Atualiza posição: D=-1 (horário), D=1 (anti-horário)
        # O operador módulo em Python garira a circularidade (0-15)
        atual = (atual + D) % 16

        if atual == H:
            print("S")
            return
        if atual == P:
            print("N")
            return

if __name__ == "__main__":
    main()