
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
        x_num = B2 - B1
        x_den = A1 - A2
        if x_num * x_den < 0:
            continue
        if x_den < 0:
            x_num = -x_num
            x_den = -x_den
        if (x_num > X2 * x_den) or (x_num < X1 * x_den):
            continue
        events.append((x_num, x_den, 0))

for i in range(N):
    A, B = lines[i]
    if A == 0:
        continue
    x_num = -B
    x_den = A
    if x_num * x_den < 0:
        continue
    if x_den < 0:
        x_num = -x_num
        x_den = -x_den
    if (x_num > X2 * x_den) or (x_num < X1 * x_den):
        continue
    events.append((x_num, x_den, 1))

events.sort(key=lambda e: (e[0] * e[1], e[1] * e[1], -e[2]))

count = 0
active = 0
prev_x_num = -1
prev_x_den = 1
for event in events:
    x_num, x_den, typ = event
    if typ == 1:
        active += 1
    else:
        if (x_num, x_den) != (prev_x_num, prev_x_den):
            count += active
            prev_x_num = x_num
            prev_x_den = x_den
        active -= 1

print(count)
