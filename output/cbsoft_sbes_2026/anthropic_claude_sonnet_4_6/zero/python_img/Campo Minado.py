n = int(input())
cells = [int(input()) for _ in range(n)]

for i in range(n):
    total = cells[i]
    if i > 0:
        total += cells[i-1]
    if i < n-1:
        total += cells[i+1]
    print(total)