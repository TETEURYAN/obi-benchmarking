import sys

data = sys.stdin.buffer.read().split()
if not data:
    sys.exit()

n = int(data[0])
m = int(data[1])

grid = bytearray(n * m)
idx = 2
pos = 0
for _ in range(n):
    for _ in range(m):
        grid[pos] = 1 if data[idx] == b'1' else 0
        idx += 1
        pos += 1

count = 0
stack = []

for i in range(n):
    base = i * m
    for j in range(m):
        p = base + j
        if grid[p]:
            count += 1
            grid[p] = 0
            stack.append(p)

            while stack:
                cur = stack.pop()
                r = cur // m
                c = cur - r * m

                if r > 0:
                    nxt = cur - m
                    if grid[nxt]:
                        grid[nxt] = 0
                        stack.append(nxt)
                if r + 1 < n:
                    nxt = cur + m
                    if grid[nxt]:
                        grid[nxt] = 0
                        stack.append(nxt)
                if c > 0:
                    nxt = cur - 1
                    if grid[nxt]:
                        grid[nxt] = 0
                        stack.append(nxt)
                if c + 1 < m:
                    nxt = cur + 1
                    if grid[nxt]:
                        grid[nxt] = 0
                        stack.append(nxt)

print(count)