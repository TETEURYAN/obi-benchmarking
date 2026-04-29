import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    n = data[0]
    w = data[1:1+n]

    reachable = [False] * n
    j = 0
    for i in range(n):
        while j < i and w[i] - w[j] > 8:
            j += 1
        if j < i:
            reachable[i] = True
        if i > 0 and reachable[i - 1]:
            reachable[i] = True

    print('S' if reachable[n - 1] else 'N')

if __name__ == "__main__":
    main()
