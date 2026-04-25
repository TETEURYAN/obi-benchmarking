import sys

data = sys.stdin.read().split()
n = int(data[0])
balls = list(map(int, data[1:n+1]))

while len(balls) > 1:
    new_balls = []
    for i in range(len(balls) - 1):
        if balls[i] == balls[i+1]:
            new_balls.append(1)
        else:
            new_balls.append(-1)
    balls = new_balls

if balls[0] == 1:
    print("preta")
else:
    print("branca")