
holes = {(1,3), (2,3), (2,5), (5,4)}
moves = [
    (0,0),
    (1,2),   # 1
    (2,1),   # 2
    (2,-1),  # 3
    (1,-2),  # 4
    (-1,-2), # 5
    (-2,-1), # 6
    (-2,1),  # 7
    (-1,2)   # 8
]

N = int(input())
seq = list(map(int, input().split()))

x, y = 4, 3
count = 0

for m in seq:
    dx, dy = moves[m]
    x += dx
    y += dy
    count += 1
    if (x, y) in holes:
        break

print(count)
