import sys

input_data = sys.stdin.read().split()
A = int(input_data[0])
B = int(input_data[1])

S = (A + 4) // 2
if (A + 4) % 2 != 0:
    print(-1, -1)
else:
    D = (S - 4) ** 2 - 4 * B
    if D < 0:
        print(-1, -1)
    else:
        sqrtD = int(D ** 0.5)
        if sqrtD * sqrtD != D:
            print(-1, -1)
        else:
            P = (S - 4 + sqrtD) // 2
            Q = (S - 4 - sqrtD) // 2
            if P < 1 or Q < 1:
                print(-1, -1)
            else:
                W = P + 2
                H = Q + 2
                if W > H:
                    W, H = H, W
                print(W, H)