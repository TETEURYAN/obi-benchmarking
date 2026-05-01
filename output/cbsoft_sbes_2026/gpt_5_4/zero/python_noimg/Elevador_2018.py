import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    n = data[0]
    w = data[1:1+n]
    w.sort()

    reachable = [False] * n
    j = 0
    for i in range(n):
        while w[i] - w[j] > 8:
            j += 1
        if i == 0:
            reachable[i] = True
        else:
            reachable[i] = any(reachable[j:i])

    print('S' if reachable[-1] else 'N')

if __name__ == "__main__":
    main()
