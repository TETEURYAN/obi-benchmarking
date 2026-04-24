import sys

input_data = sys.stdin.read().split()
N = int(input_data[0])
seq = list(map(int, input_data[1:]))
count = 0
for i in range(N - 2):
    if seq[i] == 1 and seq[i+1] == 0 and seq[i+2] == 0:
        count += 1
print(count)