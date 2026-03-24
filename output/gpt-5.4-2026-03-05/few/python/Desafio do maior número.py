import sys

data = list(map(int, sys.stdin.read().split()))
mx = 0
for x in data:
    if x == 0:
        break
    if x > mx:
        mx = x
print(mx)