H, P, F, D = map(int, input().split())

pos = F
while True:
    pos = (pos - D) % 16
    if pos == H:
        print("S")
        break
    if pos == P:
        print("N")
        break