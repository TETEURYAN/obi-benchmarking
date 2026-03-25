import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
m = int(input_data[1])
s = int(input_data[2])

for i in range(m, n - 1, -1):
    temp = i
    digit_sum = 0
    while temp > 0:
        digit_sum += temp % 10
        temp //= 10
    if digit_sum == s:
        print(i)
        exit()

print(-1)