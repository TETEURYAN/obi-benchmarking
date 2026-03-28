import sys

data = sys.stdin.read().strip().split('\n')
wins = 0
for line in data:
    if line == 'V':
        wins += 1

if wins >= 5:
    print(1)
elif wins >= 3:
    print(2)
elif wins >= 1:
    print(3)
else:
    print(-1)