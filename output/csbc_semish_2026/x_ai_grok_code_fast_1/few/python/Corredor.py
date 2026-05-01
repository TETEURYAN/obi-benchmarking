import sys

data = sys.stdin.read().split()
N = int(data[0])
vidas = list(map(int, data[1:]))

if N == 0:
    print(0)
else:
    max_so_far = vidas[0]
    max_ending_here = vidas[0]
    for i in range(1, N):
        max_ending_here = max(vidas[i], max_ending_here + vidas[i])
        max_so_far = max(max_so_far, max_ending_here)
    print(max_so_far)