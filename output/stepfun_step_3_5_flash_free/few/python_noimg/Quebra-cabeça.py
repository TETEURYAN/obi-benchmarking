import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    mapping = {}
    idx = 1
    for _ in range(n):
        e = int(data[idx])
        c = data[idx+1]
        d = int(data[idx+2])
        mapping[e] = (c, d)
        idx += 3
    current = 0
    res = []
    while current != 1:
        c, nxt = mapping[current]
        res.append(c)
        current = nxt
    print(''.join(res))

if __name__ == "__main__":
    main()