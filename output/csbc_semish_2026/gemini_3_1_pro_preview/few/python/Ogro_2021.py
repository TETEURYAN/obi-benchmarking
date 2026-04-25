import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])

left = min(n, 5)
right = max(0, n - 5)

left_str = "I" * left if left > 0 else "*"
right_str = "I" * right if right > 0 else "*"

print(left_str)
print(right_str)