import sys

data = sys.stdin.read().split()
H, P, F, D = int(data[0]), int(data[1]), int(data[2]), int(data[3])

# Simulate the fugitive moving in direction D (-1 clockwise, 1 counter-clockwise)
# Check if fugitive reaches H before P
pos = F
while True:
    pos = (pos + D) % 16
    if pos == P:
        print("N")
        break
    if pos == H:
        print("S")
        break