import sys

data = sys.stdin.read().split()
N = int(data[0])
balls = [int(x) for x in data[1:]]
current = balls
while len(current) > 1:
    next_row = []
    for i in range(len(current) - 1):
        if current[i] == current[i + 1]:
            next_row.append(1)
        else:
            next_row.append(-1)
    current = next_row
if current[0] == 1:
    print("preta")
else:
    print("branca")