import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()

n = int(data[0])
s = data[1]

best = 1

for center in range(n):
    l = r = center
    while l >= 0 and r < n and s[l] == s[r]:
        length = r - l + 1
        if length > best:
            best = length
        l -= 1
        r += 1

    l, r = center, center + 1
    while l >= 0 and r < n and s[l] == s[r]:
        length = r - l + 1
        if length > best:
            best = length
        l -= 1
        r += 1

print(best)