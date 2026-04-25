import sys

input_data = sys.stdin.read().split()
idx = 0
N = int(input_data[idx])
idx += 1
rects = []
for i in range(N):
    X1 = int(input_data[idx])
    Y1 = int(input_data[idx + 1])
    X2 = int(input_data[idx + 2])
    Y2 = int(input_data[idx + 3])
    rects.append((X1, Y1, X2, Y2))
    idx += 4

# sort by X1 asc, then Y1 desc
order = sorted(range(N), key=lambda i: (rects[i][0], -rects[i][1]))

children = [[] for _ in range(N)]
stack = []

def contains(a, b):
    ra = rects[a]
    rb = rects[b]
    return ra[0] <= rb[0] and rb[1] <= ra[1] and rb[2] <= ra[2] and ra[3] <= rb[3]

for i in order:
    while stack and not contains(stack[-1], i):
        stack.pop()
    if stack:
        parent = stack[-1]
        children[parent].append(i)
    stack.append(i)

leaves = sum(1 for c in children if not c)
print(leaves)