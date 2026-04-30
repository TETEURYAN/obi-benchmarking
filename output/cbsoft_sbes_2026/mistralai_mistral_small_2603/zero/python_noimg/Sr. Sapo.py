
from collections import deque

def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    N = int(input[ptr]); ptr += 1
    M = int(input[ptr]); ptr += 1
    P = int(input[ptr]); ptr += 1

    stones = set()
    for _ in range(P):
        c = int(input[ptr]); ptr += 1
        l = int(input[ptr]); ptr += 1
        stones.add((c, l))

    SC = int(input[ptr]); ptr += 1
    SL = int(input[ptr]); ptr += 1
    RC = int(input[ptr]); ptr += 1
    RL = int(input[ptr]); ptr += 1

    if (SC, SL) == (RC, RL):
        print('S')
        return

    visited = set()
    queue = deque()
    queue.append((SC, SL))
    visited.add((SC, SL))

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while queue:
        c, l = queue.popleft()
        for dc, dl in directions:
            for step in range(1, 4):
                nc = c + dc * step
                nl = l + dl * step
                if 1 <= nc <= N and 1 <= nl <= M:
                    if (nc, nl) == (RC, RL):
                        print('S')
                        return
                    if (nc, nl) in stones and (nc, nl) not in visited:
                        visited.add((nc, nl))
                        queue.append((nc, nl))
                else:
                    break
    print('N')

if __name__ == '__main__':
    main()
