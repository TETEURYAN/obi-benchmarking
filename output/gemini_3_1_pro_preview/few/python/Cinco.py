import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
digits = [int(x) for x in input_data[1:n+1]]

last_digit = digits[-1]
best_i = -1

for i in range(n - 1):
    if digits[i] == 0 or digits[i] == 5:
        if digits[i] < last_digit:
            best_i = i
            break

if best_i == -1:
    for i in range(n - 2, -1, -1):
        if digits[i] == 0 or digits[i] == 5:
            best_i = i
            break

if best_i == -1:
    print("-1")
else:
    digits[best_i], digits[-1] = digits[-1], digits[best_i]
    print(*(digits))