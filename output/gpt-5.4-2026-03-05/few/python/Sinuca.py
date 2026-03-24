import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()

n = int(data[0])
row = list(map(int, data[1:1 + n]))

while len(row) > 1:
    new_row = []
    for i in range(len(row) - 1):
        if row[i] == row[i + 1]:
            new_row.append(1)
        else:
            new_row.append(-1)
    row = new_row

print("preta" if row[0] == 1 else "branca")