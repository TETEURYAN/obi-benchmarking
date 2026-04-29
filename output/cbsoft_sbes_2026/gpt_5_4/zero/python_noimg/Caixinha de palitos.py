import sys

def c2(x):
    return x * (x - 1) // 2 if x >= 2 else 0

def main():
    data = sys.stdin.readline().split()
    N, M = map(int, data)

    # Número de soluções positivas de x+y+z=N com x,y,z <= M
    # Seja ai = xi-1 >= 0, então a+b+c = N-3 e ai <= M-1.
    S = N - 3
    U = M - 1

    ans = c2(S + 2) - 3 * c2(S - (U + 1) + 2) + 3 * c2(S - 2 * (U + 1) + 2) - c2(S - 3 * (U + 1) + 2)
    print(ans)

if __name__ == "__main__":
    main()
