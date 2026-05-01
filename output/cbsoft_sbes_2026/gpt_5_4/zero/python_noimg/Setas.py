import sys

def main():
    input = sys.stdin.readline
    n = int(input())
    grid = [input().strip() for _ in range(n)]

    total = n * n
    state = bytearray(total)  # 0 = unvisited, 1 = visiting, 2 = safe, 3 = unsafe

    def nxt(idx):
        i, j = divmod(idx, n)
        c = grid[i][j]
        if c == 'V':
            i += 1
        elif c == 'A':
            i -= 1
        elif c == '>':
            j += 1
        else:  # '<'
            j -= 1
        if 0 <= i < n and 0 <= j < n:
            return i * n + j
        return -1

    safe_count = 0

    for start in range(total):
        if state[start] != 0:
            continue

        path = []
        pos_in_path = {}

        cur = start
        while True:
            s = state[cur]
            if s == 0:
                state[cur] = 1
                pos_in_path[cur] = len(path)
                path.append(cur)
                nx = nxt(cur)
                if nx == -1:
                    for v in path:
                        state[v] = 3
                    break
                cur = nx
            elif s == 1:
                cycle_start = pos_in_path[cur]
                for k, v in enumerate(path):
                    if k >= cycle_start:
                        state[v] = 2
                    else:
                        state[v] = 2
                break
            elif s == 2:
                for v in path:
                    state[v] = 2
                break
            else:  # s == 3
                for v in path:
                    state[v] = 3
                break

    for v in state:
        if v == 2:
            safe_count += 1

    print(safe_count)

if __name__ == "__main__":
    main()
