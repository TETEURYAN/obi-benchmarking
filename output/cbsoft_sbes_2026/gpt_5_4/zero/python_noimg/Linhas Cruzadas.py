import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n = data[0]
    a = data[1:1+n]

    bit = [0] * (n + 1)

    def update(i, v):
        while i <= n:
            bit[i] += v
            i += i & -i

    def query(i):
        s = 0
        while i > 0:
            s += bit[i]
            i -= i & -i
        return s

    inv = 0
    seen = 0
    for x in a:
        inv += seen - query(x)
        update(x, 1)
        seen += 1

    print(inv)

if __name__ == "__main__":
    main()
