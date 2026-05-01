import math

A = int(input())
B = int(input())

# The room has white tiles in the center and one row of blue tiles on each side.
# If the total room dimensions are (w+2) x (h+2), then:
# White tiles: w * h = B
# Blue tiles: (w+2)*(h+2) - w*h = A
# (w+2)*(h+2) = w*h + 2w + 2h + 4 = B + 2w + 2h + 4
# So A = 2w + 2h + 4
# w + h = (A - 4) / 2

# We need A >= 4 and (A-4) even
if A < 4 or (A - 4) % 2 != 0:
    print(-1, -1)
else:
    s = (A - 4) // 2  # w + h = s
    # w * h = B
    # w and h are roots of x^2 - s*x + B = 0
    disc = s * s - 4 * B
    if disc < 0:
        print(-1, -1)
    else:
        sqrt_disc = int(math.isqrt(disc))
        if sqrt_disc * sqrt_disc != disc:
            print(-1, -1)
        else:
            w = (s - sqrt_disc)
            h = (s + sqrt_disc)
            if w % 2 != 0 or h % 2 != 0:
                print(-1, -1)
            else:
                w //= 2
                h //= 2
                if w <= 0 or h <= 0:
                    print(-1, -1)
                else:
                    # Room dimensions are (w+2) x (h+2)
                    dim1 = w + 2
                    dim2 = h + 2
                    if dim1 > dim2:
                        dim1, dim2 = dim2, dim1
                    print(dim1, dim2)