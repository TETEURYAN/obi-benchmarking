import sys

data = sys.stdin.read().split()
n = int(data[0])
x1, y1 = int(data[1]), int(data[2])
x2, y2 = int(data[3]), int(data[4])

half = n // 2

# Horizontal cut: one sticker in rows 1..half and other in rows half+1..n
horiz = (x1 <= half < x2) or (x2 <= half < x1)

# Vertical cut: one sticker in cols 1..half and other in cols half+1..n
vert = (y1 <= half < y2) or (y2 <= half < y1)

print("S" if horiz or vert else "N")