import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()

n = int(data[0])
grid = data[1:1+n]

for i in range(n):
    row = grid[i]
    prev = -2
    cnt = 0
    for j, ch in enumerate(row):
        if ch == '*':
            cnt += 1
            if prev != -2 and j != prev + 1:
                print("N")
                sys.exit()
            prev = j
    if cnt > 0:
        l = row.find('*')
        r = row.rfind('*')
        if row[l:r+1].count('*') != r - l + 1:
            print("N")
            sys.exit()

for j in range(n):
    first = -1
    last = -1
    for i in range(n):
        if grid[i][j] == '*':
            if first == -1:
                first = i
            last = i
    if first != -1:
        for i in range(first, last + 1):
            if grid[i][j] != '*':
                print("N")
                sys.exit()

print("S")