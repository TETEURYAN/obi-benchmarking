import sys

def main():
    input = sys.stdin.readline
    n = int(input())
    grid = [input().strip() for _ in range(n)]

    total = n * n
    state = [0] * total  # 0 = unvisited, 1 = visiting, 2 = safe, 3 = unsafe

    def nxt(idx):
        i = idx // n
        j = idx % n
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
            if cur == -1:
                result = 3
                break
            if state[cur] == 2 or state[cur] == 3:
                result = state[cur]
                break
            if cur in pos_in_path:
                result = 2
                break

            pos_in_path[cur] = len(path)
            path.append(cur)
            state[cur] = 1
            cur = nxt(cur)

        for v in path:
            state[v] = result
            if result == 2:
                safe_count += 1

    print(safe_count)

if __name__ == "__main__":
    main()
