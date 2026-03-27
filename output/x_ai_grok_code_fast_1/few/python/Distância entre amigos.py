import sys

input_data = sys.stdin.read().split()
N = int(input_data[0])
A = list(map(int, input_data[1:]))

val1 = [A[i] + (i + 1) for i in range(N)]
val2 = [A[i] - (i + 1) for i in range(N)]

# Find max and second max for val1
max_val1 = float('-inf')
second_max_val1 = float('-inf')
idx_max_val1 = -1
for i in range(N):
    if val1[i] > max_val1:
        second_max_val1 = max_val1
        max_val1 = val1[i]
        idx_max_val1 = i
    elif val1[i] > second_max_val1:
        second_max_val1 = val1[i]

# Find max and second max for val2
max_val2 = float('-inf')
second_max_val2 = float('-inf')
idx_max_val2 = -1
for i in range(N):
    if val2[i] > max_val2:
        second_max_val2 = max_val2
        max_val2 = val2[i]
        idx_max_val2 = i
    elif val2[i] > second_max_val2:
        second_max_val2 = val2[i]

candidates = [max_val1 + max_val2]
if idx_max_val1 == idx_max_val2:
    candidates.append(max_val1 + second_max_val2)
    candidates.append(second_max_val1 + max_val2)

print(max(candidates))