import sys

data = sys.stdin.read().split()
N = int(data[0])
P = [int(data[i+1]) for i in range(N)]
dark = [P[i] + P[(i+1)%N] < 1000 for i in range(N)]
positions = [i for i in range(N) if not dark[i]]
if not positions:
    print(N)
else:
    max_len = 0
    for j in range(len(positions)-1):
        length = positions[j+1] - positions[j] - 1
        if length > max_len:
            max_len = length
    length = (positions[0] + N) - positions[-1] - 1
    if length > max_len:
        max_len = length
    print(max_len)