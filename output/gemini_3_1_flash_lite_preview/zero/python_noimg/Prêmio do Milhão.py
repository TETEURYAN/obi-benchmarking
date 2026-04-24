import sys

def solve():
    n = int(sys.stdin.readline())
    soma = 0
    for i in range(1, n + 1):
        acessos = int(sys.stdin.readline())
        soma += acessos
        if soma >= 1000000:
            print(i)
            break

if __name__ == '__main__':
    solve()