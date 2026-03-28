import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    idx = 0
    N = int(data[idx]); idx += 1
    pesos = []
    for _ in range(N):
        pesos.append(int(data[idx])); idx += 1
    soma = sum(pesos)
    alvo = soma // N
    for p in pesos:
        print(alvo - p)

if __name__ == "__main__":
    main()