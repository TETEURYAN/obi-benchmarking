n = int(input())
for i in range(n):
    row = []
    for j in range(n):
        val = min(i+1, j+1, n-i, n-j)
        row.append(str(val))
    print(' '.join(row))