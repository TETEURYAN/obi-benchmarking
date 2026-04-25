import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    T = [int(next(it)) for _ in range(M)]
    T_rev = T[::-1]
    convidados = []
    for p in range(1, 10001):
        k = p
        for t in T_rev:
            if k > N:
                break
            k += (k - 1) // (t - 1)
        if k > N:
            break
        convidados.append(k)
    sys.stdout.write("\n".join(map(str, convidados)))

if __name__ == "__main__":
    main()