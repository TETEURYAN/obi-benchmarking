import sys
import bisect

input_data = sys.stdin.read().split()
N = int(input_data[0])
pesos = list(map(int, input_data[1:]))
pesos.sort()
contrapesos = [0]
moved = set()
for w in pesos:
    left = w - 8
    right = w + 8
    idx = bisect.bisect_left(contrapesos, left)
    if idx < len(contrapesos) and contrapesos[idx] <= right:
        moved.add(w)
        bisect.insort(contrapesos, w)
if len(moved) == N:
    print("S")
else:
    print("N")