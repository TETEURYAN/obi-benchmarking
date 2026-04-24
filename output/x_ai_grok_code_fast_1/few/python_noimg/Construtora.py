import sys

input_data = sys.stdin.read().split()
N = int(input_data[0])
a = list(map(int, input_data[1:]))
H = max(a)
d = [H - x for x in a]
count = 0
for i in range(1, N):
    if d[i] != d[i-1]:
        count += 1
print(count)