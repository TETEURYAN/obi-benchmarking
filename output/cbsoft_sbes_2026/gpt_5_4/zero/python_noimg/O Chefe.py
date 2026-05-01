import sys

def main():
    input = sys.stdin.readline

    NMI = input().split()
    if not NMI:
        return
    N, M, I = map(int, NMI)

    age = [0] + list(map(int, input().split()))

    # Original graph over positions: manager position -> subordinate position
    out = [[] for _ in range(N + 1)]
    rev = [[] for _ in range(N + 1)]  # subordinate position -> manager positions

    for _ in range(M):
        x, y = map(int, input().split())
        out[x].append(y)
        rev[y].append(x)

    # pos_of_emp[e] = current position occupied by employee e
    # emp_at_pos[p] = employee currently at position p
    pos_of_emp = list(range(N + 1))
    emp_at_pos = list(range(N + 1))

    ans = []
    visited = [0] * (N + 1)
    mark = 0

    for _ in range(I):
        parts = input().split()
        if parts[0] == 'T':
            a = int(parts[1])
            b = int(parts[2])

            pa = pos_of_emp[a]
            pb = pos_of_emp[b]

            pos_of_emp[a], pos_of_emp[b] = pb, pa
            emp_at_pos[pa], emp_at_pos[pb] = b, a
        else:
            e = int(parts[1])
            start_pos = pos_of_emp[e]

            mark += 1
            stack = rev[start_pos][:]
            best = 10**9

            while stack:
                u = stack.pop()
                if visited[u] == mark:
                    continue
                visited[u] = mark

                emp = emp_at_pos[u]
                if age[emp] < best:
                    best = age[emp]

                for v in rev[u]:
                    if visited[v] != mark:
                        stack.append(v)

            if best == 10**9:
                ans.append('*')
            else:
                ans.append(str(best))

    sys.stdout.write('\n'.join(ans))

if __name__ == "__main__":
    main()
