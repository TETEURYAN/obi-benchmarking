import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()

n = int(data[0])
s = data[1]

res = []
count = 1

for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        count += 1
    else:
        res.append(str(count))
        res.append(s[i - 1])
        count = 1

res.append(str(count))
res.append(s[-1])

print(' '.join(res))