import sys
import math

data = sys.stdin.read().split()
if not data:
    sys.exit()

n = int(data[0])

if n <= 3:
    print('N')
else:
    r = math.isqrt(n)
    if r * r == n:
        print('S')
    else:
        ans = 'N'
        limit = r
        d = 2
        while d <= limit:
            if n % d == 0:
                ans = 'S'
                break
            d += 1
        print(ans)