import sys

data = sys.stdin.read().split()
n = int(data[0])
s = data[1]

result = []
i = 0
while i < len(s):
    c = s[i]
    count = 1
    while i + count < len(s) and s[i + count] == c:
        count += 1
    result.append(f"{count} {c}")
    i += count

print(' '.join(result))