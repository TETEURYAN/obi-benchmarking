import sys
data = sys.stdin.read().split()
wins = data.count('V')
if wins >= 5:
    print(1)
elif wins >= 3:
    print(2)
elif wins >= 1:
    print(3)
else:
    print(-1)