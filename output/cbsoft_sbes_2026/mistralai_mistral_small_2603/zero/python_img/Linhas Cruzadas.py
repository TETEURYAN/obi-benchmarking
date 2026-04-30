
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    horizontal = list(map(int, data[1:1+n]))

    pos = [0] * (n + 1)
    for idx, val in enumerate(horizontal):
        pos[val] = idx

    fenwick = [0] * (n + 1)
    def update(i, delta):
        while i <= n:
            fenwick[i] += delta
            i += i & -i

    def query(i):
        res = 0
        while i > 0:
            res += fenwick[i]
            i -= i & -i
        return res

    inversions = 0
    for i in range(n, 0, -1):
        inversions += query(pos[i])
        update(pos[i] + 1, 1)

    print(inversions)

if __name__ == "__main__":
    main()
