
import sys

N = int(sys.stdin.readline().strip())

if N == 0:
    print(4)
    sys.exit(0)

side = (1 << N) + 1
total = side * side
print(total)
