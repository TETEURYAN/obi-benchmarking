import sys

def main():
    data = sys.stdin.read().strip().split()
    notas = list(map(float, data))
    notas.sort()
    soma = notas[1] + notas[2] + notas[3]
    print(f"{soma:.1f}")

if __name__ == "__main__":
    main()