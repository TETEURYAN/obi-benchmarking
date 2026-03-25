import sys
import math

data = sys.stdin.read().split()
if not data:
    sys.exit()

N = int(data[0])
M = int(data[1])

g = math.gcd(N, M)
ans = M // g

while True:
    x = ans * g - 1
    if x <= M and math.gcd(N, x) == 1:
        print(x)
        break
    ans -= 1