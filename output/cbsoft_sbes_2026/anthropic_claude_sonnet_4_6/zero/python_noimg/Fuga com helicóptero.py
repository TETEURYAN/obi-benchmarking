H, P, F, D = map(int, input().split())

# Simulate the fugitive's path
current = F
while True:
    current = (current + D) % 16
    if current == P:
        print("N")
        break
    if current == H:
        print("S")
        break