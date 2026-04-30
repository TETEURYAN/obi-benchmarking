
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
H = [int(x) for x in data[1:]]

if N == 0:
    print(0)
    sys.exit()

max_h = max(H)
min_h = min(H)

if max_h == min_h:
    print(N)
    sys.exit()

left_max = [0] * N
right_max = [0] * N

left_max[0] = H[0]
for i in range(1, N):
    left_max[i] = max(left_max[i-1], H[i])

right_max[N-1] = H[N-1]
for i in range(N-2, -1, -1):
    right_max[i] = max(right_max[i+1], H[i])

count = 0
for i in range(N):
    water_level = min(left_max[i], right_max[i])
    if water_level > H[i]:
        count += 1

print(count)
