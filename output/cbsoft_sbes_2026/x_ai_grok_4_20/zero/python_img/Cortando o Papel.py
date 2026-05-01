
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
A = list(map(int, data[1:]))

if N == 0:
    print(0)
    sys.exit(0)

max_pieces = 1
current_max = A[0]
current_min = A[0]
max_so_far = A[0]
min_so_far = A[0]

for i in range(1, N):
    if A[i] > current_max:
        current_max = A[i]
        max_so_far = max(max_so_far, current_max)
    elif A[i] < current_min:
        current_min = A[i]
        min_so_far = min(min_so_far, current_min)
    else:
        max_pieces = max(max_pieces, i)
        current_max = A[i]
        current_min = A[i]
        max_so_far = A[i]
        min_so_far = A[i]

max_pieces = max(max_pieces, N)

print(max_pieces)
