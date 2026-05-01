import sys

s = sys.stdin.readline().rstrip('\n')
res = []
i = 0
n = len(s)

while i < n:
    if s[i] == ' ':
        res.append(' ')
        i += 1
    else:
        res.append(s[i + 1])
        i += 2

print(''.join(res))