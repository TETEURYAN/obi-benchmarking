holes = {(1,3), (2,3), (2,5), (5,4)}
start = (4, 3)

# From the figure, movements 1-8 from position (x,y):
# Looking at figure 1(b), the knight is at 0, and moves are numbered 1-8
# Move 1: top-right (+2, +1) -> from (4,3) to (6,4)? Let me analyze from the example
# Example: move 1 from (4,3) -> (5,5): dx=+1, dy=+2
# Move 8 from (5,5) -> (4,7): dx=-1, dy=+2
# Move 5 from (4,7) -> (3,5): dx=-1, dy=-2
# Move 3 from (3,5) -> (5,4): dx=+2, dy=-1
# So move 3 leads to hole (5,4) - confirmed

# Let me map all 8 moves:
# From figure: 1 is top-right area, going clockwise or specific pattern
# Move 1: (4,3)->(5,5): (+1,+2)
# Move 8: (5,5)->(4,7): (-1,+2)
# Move 5: (4,7)->(3,5): (-1,-2)
# Move 3: (3,5)->(5,4): (+2,-1)

# Second example: move 6 from (4,3)->(2,2): (-2,-1)
# Move 8 from (2,2)->(1,4): (-1,+2)
# Move 1 from (1,4)->(2,6): (+1,+2)

# So:
# 1: (+1,+2)
# 8: (-1,+2)
# 5: (-1,-2)
# 3: (+2,-1)
# 6: (-2,-1)

# From figure 1(b) layout (clockwise from top-right):
# 1: (+1,+2)
# 2: (+2,+1)
# 3: (+2,-1)
# 4: (+1,-2)
# 5: (-1,-2)
# 6: (-2,-1)
# 7: (-2,+1)
# 8: (-1,+2)

moves = {
    1: (1, 2),
    2: (2, 1),
    3: (2, -1),
    4: (1, -2),
    5: (-1, -2),
    6: (-2, -1),
    7: (-2, 1),
    8: (-1, 2)
}

n = int(input())
ms = list(map(int, input().split()))

x, y = start
count = 0
for m in ms:
    dx, dy = moves[m]
    x += dx
    y += dy
    count += 1
    if (x, y) in holes:
        break

print(count)