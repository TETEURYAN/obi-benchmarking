import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
L = [int(x) for x in input_data[1:n+1]]

P = [0] * n
current_sum = 0
for i in range(n):
    P[i] = current_sum
    current_sum += L[i]

C = current_sum
if C % 2 != 0:
    print('N')
    exit()

H = C // 2

count = 0
i = 0
j = 0

while i < n and P[i] < H:
    target = P[i] + H
    while j < n and P[j] < target:
        j += 1
    if j < n and P[j] == target:
        count += 1
        if count >= 2:
            print('S')
            exit()
    i += 1

print('N')