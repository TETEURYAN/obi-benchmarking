
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    trees = []
    index = 1
    for i in range(n):
        x = int(data[index])
        h = int(data[index + 1])
        trees.append((x, h))
        index += 2

    trees.sort()
    q = deque()
    q.append((0, trees[0][1]))
    for i in range(1, n):
        while len(q) >= 2:
            x1, h1 = q[-2]
            x2, h2 = q[-1]
            xi, hi = trees[i]
            if (hi - h2) * (x2 - x1) >= (h2 - h1) * (xi - x2):
                q.pop()
            else:
                break
        q.append((i, trees[i][1]))

    jumps = 0
    current = n - 1
    while current != 0:
        next_pos = -1
        for i in range(len(q)):
            pos, _ = q[i]
            if pos < current:
                next_pos = pos
            else:
                break
        if next_pos == -1:
            break
        jumps += 1
        current = next_pos

    print(jumps)

if __name__ == "__main__":
    main()
