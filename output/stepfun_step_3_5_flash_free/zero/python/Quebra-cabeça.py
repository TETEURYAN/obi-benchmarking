
import sys

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    left_map = {}
    for i in range(1, n + 1):
        e, c, d = data[i].split()
        left_map[int(e)] = (c, int(d))
    current = 0
    res = []
    while current in left_map:
        c, d = left_map[current]
        res.append(c)
        current = d
    print(''.join(res))

if __name__ == "__main__":
    main()
