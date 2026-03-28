import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    a, b, c = map(int, data)
    # O vice-campeão é o segundo maior entre os três
    # Podemos somar todos e subtrair o maior e o menor
    total = a + b + c
    maior = max(a, b, c)
    menor = min(a, b, c)
    vice = total - maior - menor
    print(vice)

if __name__ == "__main__":
    main()