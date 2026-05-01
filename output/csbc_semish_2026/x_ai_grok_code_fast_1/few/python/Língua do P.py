import sys

s = sys.stdin.read().strip()
result = []
i = 0
while i < len(s):
    if s[i] == 'p' and i + 1 < len(s) and s[i + 1].isalpha():
        result.append(s[i + 1])
        i += 2
    else:
        result.append(s[i])
        i += 1
print(''.join(result))