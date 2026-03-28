import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    idx = 0
    N = int(data[idx]); idx += 1
    estoque = [0] * (N + 1)
    for i in range(1, N + 1):
        estoque[i] = int(data[idx]); idx += 1
    P = int(data[idx]); idx += 1
    vendidos = 0
    for _ in range(P):
        I = int(data[idx]); idx += 1
        if estoque[I] > 0:
            estoque[I] -= 1
            vendidos += 1
    print(vendidos)

if __name__ == "__main__":
    main()