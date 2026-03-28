import sys

input_data = sys.stdin.read().split()
A = input_data[0]
B = input_data[1]
max_len = max(len(A), len(B))
A_digits = list(A.zfill(max_len))
B_digits = list(B.zfill(max_len))
for i in range(max_len - 1, -1, -1):
    if A_digits[i] < B_digits[i]:
        A_digits.pop(i)
    elif B_digits[i] < A_digits[i]:
        B_digits.pop(i)
A_num = int(''.join(A_digits)) if A_digits else -1
B_num = int(''.join(B_digits)) if B_digits else -1
nums = sorted([A_num, B_num])
print(nums[0], nums[1])