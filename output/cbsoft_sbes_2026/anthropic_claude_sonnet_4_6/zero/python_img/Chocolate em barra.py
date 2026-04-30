n = int(input())
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

half = n // 2

# Check horizontal cut: one figurinha in rows 1..half and other in rows half+1..n
horizontal = (x1 <= half and x2 > half) or (x2 <= half and x1 > half)

# Check vertical cut: one figurinha in cols 1..half and other in cols half+1..n
vertical = (y1 <= half and y2 > half) or (y2 <= half and y1 > half)

if horizontal or vertical:
    print("S")
else:
    print("N")