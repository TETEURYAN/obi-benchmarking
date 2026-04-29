import sys

def main():
    input = sys.stdin.readline

    first = input().split()
    if not first:
        return
    n, m, q = map(int, first)

    age = [0] + list(map(int, input().split()))

    g = [[False] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        x, y = map(int, input().split())
        g[x][y] = True

    pos_to_emp = list(range(n + 1))
    emp_to_pos = list(range(n + 1))

    out = []

    for _ in range(q):
        parts = input().split()
        if parts[0] == 'T':
            a = int(parts[1])
            b = int(parts[2])
            pa = emp_to_pos[a]
            pb = emp_to_pos[b]
            pos_to_emp[pa], pos_to_emp[pb] = pos_to_emp[pb], pos_to_emp[pa]
            emp_to_pos[a], emp_to_pos[b] = pb, pa
        else:
            e = int(parts[1])
            pe = emp_to_pos[e]

            visited = [False] * (n + 1)
            stack = []

            for manager_pos in range(1, n + 1):
                if g[manager_pos][pe]:
                    visited[manager_pos] = True
                    stack.append(manager_pos)

            if not stack:
                out.append('*')
                continue

            best = 10**9
            while stack:
                u = stack.pop()
                emp = pos_to_emp[u]
                if age[emp] < best:
                    best = age[emp]
                for v in range(1, n + 1):
                    if g[v][u] and not visited[v]:
                        visited[v] = True
                        stack.append(v)

            out.append(str(best))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()