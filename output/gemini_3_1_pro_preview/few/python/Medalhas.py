import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

t1 = int(input_data[0])
t2 = int(input_data[1])
t3 = int(input_data[2])

times = [(t1, 1), (t2, 2), (t3, 3)]
times.sort()

for t, idx in times:
    print(idx)