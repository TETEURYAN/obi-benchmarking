n = int(input())
total = 0
for _ in range(n):
    c, s = map(int, input().split())
    diff = abs(c - s)
    total += min(diff, 10 - diff)
print(total)