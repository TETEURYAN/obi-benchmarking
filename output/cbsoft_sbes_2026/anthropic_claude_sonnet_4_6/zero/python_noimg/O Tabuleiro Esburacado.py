n = int(input())
moves = list(map(int, input().split()))

# Knight moves numbered 1-8
# From the figure, the moves are:
# Move 1: (+1, +2)
# Move 2: (+2, +1)
# Move 3: (+2, -1)
# Move 4: (+1, -2)
# Move 5: (-1, -2)
# Move 6: (-2, -1)
# Move 7: (-2, +1)
# Move 8: (-1, +2)

move_map = {
    1: (1, 2),
    2: (2, 1),
    3: (2, -1),
    4: (1, -2),
    5: (-1, -2),
    6: (-2, -1),
    7: (-2, 1),
    8: (-1, 2)
}

holes = {(1, 3), (2, 3), (2, 5), (5, 4)}

x, y = 4, 3
count = 0

for m in moves:
    dx, dy = move_map[m]
    x += dx
    y += dy
    count += 1
    if (x, y) in holes:
        break

print(count)