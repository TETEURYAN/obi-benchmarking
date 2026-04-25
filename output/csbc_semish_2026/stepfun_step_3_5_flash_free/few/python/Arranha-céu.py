import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    q = int(next(it))
    A = [0] * (n + 1)
    tree = [0] * (n + 1)

    def update(i, delta):
        while i <= n:
            tree[i] += delta
            i += i & -i

    def query(i):
        s = 0
        while i:
            s += tree[i]
            i -= i & -i
        return s

    for i in range(1, n + 1):
        val = int(next(it))
        A[i] = val
        update(i, val)

    output = []
    for _ in range(q):
        t = int(next(it))
        if t == 0:
            k = int(next(it))
            p = int(next(it))
            delta = p - A[k]
            A[k] = p
            update(k, delta)
        else:
            k = int(next(it))
            output.append(str(query(k)))

    sys.stdout.write("\n".join(output))

if __name__ == "__main__":
    main()