n = int(input())
balls = list(map(int, input().split()))

while len(balls) > 1:
    new_balls = []
    for i in range(len(balls) - 1):
        if balls[i] == balls[i+1]:
            new_balls.append(1)
        else:
            new_balls.append(-1)
    balls = new_balls

print("preta" if balls[0] == 1 else "branca")