import math

A = int(input())
B = int(input())

# The room has white tiles in center and one row of blue tiles on each side
# If the total room dimensions are (W+2) x (H+2), then:
# White tiles: W * H = B
# Blue tiles: (W+2)*(H+2) - W*H = 2W + 2H + 4 = A
# So: 2W + 2H + 4 = A => W + H = (A - 4) / 2
# And W * H = B

# W and H are roots of: x^2 - (W+H)x + W*H = 0
# x^2 - S*x + B = 0 where S = (A-4)/2

if (A - 4) % 2 != 0:
    print(-1, -1)
else:
    S = (A - 4) // 2
    # W + H = S, W * H = B
    # discriminant = S^2 - 4B
    disc = S * S - 4 * B
    if disc < 0:
        print(-1, -1)
    else:
        sqrt_disc = int(math.isqrt(disc))
        if sqrt_disc * sqrt_disc != disc:
            print(-1, -1)
        else:
            W = (S - sqrt_disc)
            H = (S + sqrt_disc)
            if W % 2 != 0 or H % 2 != 0:
                print(-1, -1)
            else:
                W //= 2
                H //= 2
                if W <= 0 or H <= 0:
                    print(-1, -1)
                else:
                    # Verify
                    if W * H == B and 2*W + 2*H + 4 == A:
                        # Output dimensions of the room (including blue border)
                        rw = W + 2
                        rh = H + 2
                        if rw <= rh:
                            print(rw, rh)
                        else:
                            print(rh, rw)
                    else:
                        print(-1, -1)