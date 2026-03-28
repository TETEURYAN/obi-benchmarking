import sys

D = int(sys.stdin.read().strip())
r = D % 400
print(min(r, 400 - r))