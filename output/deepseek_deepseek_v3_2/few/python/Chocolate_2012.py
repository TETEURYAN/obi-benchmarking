import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    L = int(data[0])
    # Cada divisão transforma um quadrado em 4 quadrados menores.
    # O processo para quando o lado for menor que 2.
    # O número de divisões é quantas vezes podemos dividir L por 2 até chegar a 1.
    # Número de pedaços finais = 4 ** (número de divisões)
    # Número de divisões = floor(log2(L)) porque a última divisão ocorre quando lado >= 2.
    # Exemplo: L=4 -> log2(4)=2 -> 4**2=16.
    # L=9 -> log2(9)≈3.17 -> floor=3 -> 4**3=64.
    # L=2 -> log2(2)=1 -> 4**1=4.
    # Para L=1 (não ocorre no problema) seria 4**0=1.
    divisoes = 0
    while L >= 2:
        L //= 2
        divisoes += 1
    resultado = 4 ** divisoes
    print(resultado)

if __name__ == "__main__":
    main()