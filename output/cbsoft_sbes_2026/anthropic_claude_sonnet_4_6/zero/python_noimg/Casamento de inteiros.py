A = list(input().strip())
B = list(input().strip())

# Equalize lengths with leading zeros
len_a = len(A)
len_b = len(B)
max_len = max(len_a, len_b)

A = ['0'] * (max_len - len_a) + A
B = ['0'] * (max_len - len_b) + B

# Process from least significant to most significant (right to left)
# We'll work with indices from right to left
remaining_a = list(A)
remaining_b = list(B)

# We need to track which digits are eliminated
# Process from index max_len-1 down to 0
eliminated_a = [False] * max_len
eliminated_b = [False] * max_len

for i in range(max_len - 1, -1, -1):
    da = int(A[i])
    db = int(B[i])
    if da < db:
        eliminated_a[i] = True
    elif db < da:
        eliminated_b[i] = True
    # if equal, neither is eliminated

# Build remaining digits
res_a = []
for i in range(max_len):
    if not eliminated_a[i]:
        res_a.append(A[i])

res_b = []
for i in range(max_len):
    if not eliminated_b[i]:
        res_b.append(B[i])

# Convert to numbers
def digits_to_num(digits):
    if not digits:
        return -1
    # Remove leading zeros but keep at least one digit
    s = ''.join(digits).lstrip('0')
    if s == '':
        return 0
    return int(s)

num_a = digits_to_num(res_a)
num_b = digits_to_num(res_b)

# Output in non-decreasing order
if num_a <= num_b:
    print(num_a, num_b)
else:
    print(num_b, num_a)