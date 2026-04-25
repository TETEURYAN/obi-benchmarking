import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()

n = int(data[0])
m = int(data[1])
limit2 = m * m

x = 0
y = 0
i = 2

for _ in range(n):
    c = data[i]
    d = int(data[i + 1])
    i += 2

    if c == 'N':
        y += d
    elif c == 'S':
        y -= d
    elif c == 'L':
        x += d
    else:  # 'O'
        x -= d

    if x * x + y * y > limit2:
        print(1)
        sys.exit()

print(0)