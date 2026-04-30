
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
A = list(map(int, data[1:]))

total = sum(A)
if total % 2 != 0:
    print(-1)
    sys.exit(0)

target_sum = total // 2

min_moves = float('inf')
found = False

for h in range(1, 10001):
    expected = [h + i for i in range(N)]
    s = sum(expected)
    if s != target_sum:
        continue
    moves = 0
    for i in range(N):
        if A[i] > expected[i]:
            moves += A[i] - expected[i]
    if moves < min_moves:
        min_moves = moves
    found = True

if found:
    print(min_moves)
else:
    print(-1)
