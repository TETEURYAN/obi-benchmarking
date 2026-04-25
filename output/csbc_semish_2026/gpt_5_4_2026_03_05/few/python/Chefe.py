import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()

it = iter(data)
n = int(next(it))
m = int(next(it))
q = int(next(it))

age = [0] + [int(next(it)) for _ in range(n)]

orig = [[False] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    x = int(next(it))
    y = int(next(it))
    orig[x][y] = True

pos_to_emp = list(range(n + 1))
emp_to_pos = list(range(n + 1))

out = []

for _ in range(q):
    typ = next(it)
    if typ == 'T':
        a = int(next(it))
        b = int(next(it))
        pa = emp_to_pos[a]
        pb = emp_to_pos[b]
        if pa != pb:
            pos_to_emp[pa], pos_to_emp[pb] = pos_to_emp[pb], pos_to_emp[pa]
            emp_to_pos[a], emp_to_pos[b] = pb, pa
    else:
        e = int(next(it))
        start = emp_to_pos[e]
        visited = [False] * (n + 1)
        stack = [start]
        visited[start] = True
        best = 10**9

        while stack:
            v = stack.pop()
            for u in range(1, n + 1):
                if orig[u][v] and not visited[u]:
                    visited[u] = True
                    emp = pos_to_emp[u]
                    if age[emp] < best:
                        best = age[emp]
                    stack.append(u)

        if best == 10**9:
            out.append('*')
        else:
            out.append(str(best))

sys.stdout.write('\n'.join(out))