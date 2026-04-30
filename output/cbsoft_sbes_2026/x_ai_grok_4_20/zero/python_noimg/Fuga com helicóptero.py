
H, P, F, D = map(int, input().split())

if D == -1:
    pos = F
    while True:
        pos = (pos - 1) % 16
        if pos == H:
            print("S")
            break
        if pos == P:
            print("N")
            break
else:
    pos = F
    while True:
        pos = (pos + 1) % 16
        if pos == H:
            print("S")
            break
        if pos == P:
            print("N")
            break
