import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    N = int(data[0])
    # número de peças = (N+1)*(N+2)//2
    # pois são combinações com repetição de N+1 valores tomados 2 a 2
    pecas = (N + 1) * (N + 2) // 2
    print(pecas)

if __name__ == "__main__":
    main()