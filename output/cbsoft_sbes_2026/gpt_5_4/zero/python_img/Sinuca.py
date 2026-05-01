import sys

data = list(map(int, sys.stdin.read().split()))
n = data[0]
row = data[1:1+n]

while len(row) > 1:
    row = [row[i] * row[i + 1] for i in range(len(row) - 1)]

print("preta" if row[0] == 1 else "branca")