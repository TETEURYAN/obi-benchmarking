
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
X1 = int(data[1])
X2 = int(data[2])

lines = []
index = 3
for i in range(N):
    A = int(data[index])
    B = int(data[index + 1])
    lines.append((A, B))
    index += 2

events = []

for i in range(N):
    for j in range(i + 1, N):
        A1, B1 = lines[i]
        A2, B2 = lines[j]
        if A1 == A2:
            continue
        dx = A1 - A2
        dy = B2 - B1
        if dx > 0:
            num = dy
            den = dx
        else:
            num = -dy
            den = -dx
        events.append((num, den, i, j))

def compare(a, b):
    na, da = a
    nb, db = b
    return na * db < nb * da

events.sort(key=lambda e: (e[0] * X2 < e[1] * (X2 - X1) if e[1] > 0 else False, compare((e[0], e[1]), (0, 1)), e[0] * X1 > e[1] * (X1 - X2) if e[1] > 0 else False))

count = 0
for ev in events:
    num, den, i, j = ev
    if den == 0:
        continue
    if num * (X2 - X1) >= 0 and num * (X1 - X2) <= 0 and num * den > 0 or (num == 0 and den > 0):
        if X1 * den <= num <= X2 * den:
            count += 1

print(count)
``` 

Wait, this is incorrect. Let me provide the correct solution.

```python
import sys

input = sys.stdin.read
data = input().split()

index = 0
N = int(data[index])
X1 = int(data[index + 1])
X2 = int(data[index + 2])
index += 3

lines = []
for i in range(N):
    A = int(data[index])
    B = int(data[index + 1])
    lines.append((A, B))
    index += 2

intersections = 0

for i in range(N):
    for j in range(i + 1, N):
        a1, b1 = lines[i]
        a2, b2 = lines[j]
        if a1 == a2:
            continue
        # x = (b2 - b1) / (a1 - a2)
        num = b2 - b1
        den = a1 - a2
        if den < 0:
            num = -num
            den = -den
        if num >= X1 * den and num <= X2 * den:
            intersections += 1

print(intersections)
