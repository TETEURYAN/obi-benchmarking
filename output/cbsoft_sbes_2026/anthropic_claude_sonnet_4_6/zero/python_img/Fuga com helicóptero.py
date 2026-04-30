H, P, F, D = map(int, input().split())

# D = -1 means clockwise (decreasing numbers, mod 16)
# D = 1 means anti-clockwise (increasing numbers, mod 16)

# Simulate the fugitive's path
pos = F
escaped = False
caught = False

for _ in range(16):
    pos = (pos + D) % 16
    if pos == P:
        caught = True
        break
    if pos == H:
        escaped = True
        break

if escaped and not caught:
    print("S")
else:
    print("N")