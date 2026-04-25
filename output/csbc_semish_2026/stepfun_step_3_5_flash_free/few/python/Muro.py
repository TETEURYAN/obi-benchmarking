import sys

MOD = 10**9 + 7

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    N = int(data[0])
    if N == 0:
        print(1)
        return
    if N == 1:
        print(1)
        return
    if N == 2:
        print(5)
        return
    f0, f1, f2 = 1, 1, 5
    for i in range(3, N + 1):
        f3 = (f2 + 4 * f1 + 2 * f0) % MOD
        f0, f1, f2 = f1, f2, f3
    print(f2)

if __name__ == "__main__":
    main()