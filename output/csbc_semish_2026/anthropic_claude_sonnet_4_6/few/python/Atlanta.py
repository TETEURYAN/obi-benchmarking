import sys

def solve():
    data = sys.stdin.read().split()
    A = int(data[0])
    B = int(data[1])
    
    # The room has dimensions (w+2) x (h+2) total (including blue border)
    # where w x h is the white area (w <= h)
    # Blue tiles: total - white = (w+2)*(h+2) - w*h = 2w + 2h + 4 = A
    # White tiles: w*h = B
    
    # So: 2w + 2h + 4 = A => w + h = (A - 4) / 2
    # And: w * h = B
    
    if (A - 4) % 2 != 0:
        print(-1, -1)
        return
    
    s = (A - 4) // 2  # w + h
    p = B             # w * h
    
    if s < 0:
        print(-1, -1)
        return
    
    # w and h are roots of x^2 - s*x + p = 0
    disc = s * s - 4 * p
    if disc < 0:
        print(-1, -1)
        return
    
    sqrt_disc = int(disc ** 0.5)
    # Check around sqrt_disc for integer square root
    for candidate in [sqrt_disc - 1, sqrt_disc, sqrt_disc + 1]:
        if candidate >= 0 and candidate * candidate == disc:
            sqrt_disc = candidate
            break
    else:
        print(-1, -1)
        return
    
    if sqrt_disc * sqrt_disc != disc:
        print(-1, -1)
        return
    
    # w = (s - sqrt_disc) / 2, h = (s + sqrt_disc) / 2
    if (s - sqrt_disc) % 2 != 0:
        print(-1, -1)
        return
    
    w = (s - sqrt_disc) // 2
    h = (s + sqrt_disc) // 2
    
    if w <= 0 or h <= 0:
        print(-1, -1)
        return
    
    # Verify
    if w * h != B or 2 * w + 2 * h + 4 != A:
        print(-1, -1)
        return
    
    print(w, h)

solve()