import sys

data = list(map(int, sys.stdin.read().split()))
cnt = [0] * 10
for x in data:
    cnt[x] += 1

mx = max(cnt)
print("S" if mx <= (8 + 1) // 2 else "N")