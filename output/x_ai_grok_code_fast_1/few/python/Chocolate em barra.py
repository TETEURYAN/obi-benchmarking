import sys

input_data = sys.stdin.read().split()
N = int(input_data[0])
X1 = int(input_data[1])
Y1 = int(input_data[2])
X2 = int(input_data[3])
Y2 = int(input_data[4])

half = N // 2

# Check vertical cut: columns
vertical_possible = (Y1 <= half and Y2 > half) or (Y1 > half and Y2 <= half)

# Check horizontal cut: rows
horizontal_possible = (X1 <= half and X2 > half) or (X1 > half and X2 <= half)

if vertical_possible or horizontal_possible:
    print("S")
else:
    print("N")