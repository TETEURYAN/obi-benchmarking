import sys

input_data = sys.stdin.read().split()
N = int(input_data[0])
L = int(input_data[1])
R = int(input_data[2])
a = list(map(int, input_data[3:]))
a.sort()

min_dist_L = min(abs(x - L) for x in a)
min_dist_R = min(abs(x - R) for x in a)

max_gap = 0
for i in range(N - 1):
    gap = (a[i + 1] - a[i]) // 2
    max_gap = max(max_gap, gap)

print(max(min_dist_L, min_dist_R, max_gap))