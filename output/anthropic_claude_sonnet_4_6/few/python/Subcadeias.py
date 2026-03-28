import sys

data = sys.stdin.read().split()
n = int(data[0])
s = data[1]

best = 1
for i in range(n):
    # odd
    l, r = i, i
    while l > 0 and r < n-1 and s[l-1] == s[r+1]:
        l -= 1
        r += 1
    best = max(best, r - l + 1)
    # even
    if i+1 < n and s[i] == s[i+1]:
        l, r = i, i+1
        while l > 0 and r < n-1 and s[l-1] == s[r+1]:
            l -= 1
            r += 1
        best = max(best, r - l + 1)

print(best)