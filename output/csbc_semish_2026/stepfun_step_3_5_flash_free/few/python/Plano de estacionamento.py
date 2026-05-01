import sys
sys.setrecursionlimit(200000)

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    V = [int(next(it)) for _ in range(m)]

    dsu = list(range(n + 1))

    def find(x):
        if dsu[x] != x:
            dsu[x] = find(dsu[x])
        return dsu[x]

    count = 0
    for vi in V:
        if vi > n:
            vi = n
        vaga = find(vi)
        if vaga == 0:
            break
        count += 1
        dsu[vaga] = find(vaga - 1)

    print(count)

if __name__ == "__main__":
    main()