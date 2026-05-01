import sys

data = sys.stdin.read().strip().split()
n = int(data[0])
balls = list(map(int, data[1:1+n]))

while len(balls) > 1:
    balls = [1 if balls[i] == balls[i + 1] else -1 for i in range(len(balls) - 1)]

print("preta" if balls[0] == 1 else "branca")