import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()

perm = data[0].strip()
s = data[1].strip()

orig = [''] * 26
for i, ch in enumerate(perm):
    orig[ord(ch) - 97] = chr(97 + i)

print(''.join(orig[ord(c) - 97] for c in s))