import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    adj_mask = [0] * N
    for _ in range(M):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj_mask[u] |= 1 << v
        adj_mask[v] |= 1 << u

    total = 0
    size = 1 << N
    indep = [False] * size
    indep[0] = True
    for mask in range(1, size):
        lsb = mask & -mask
        i = lsb.bit_length() - 1
        prev = mask ^ (1 << i)
        if indep[prev] and (adj_mask[i] & prev) == 0:
            indep[mask] = True
            total += 1
    print(total)

if __name__ == "__main__":
    main()