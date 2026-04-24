import sys

data = sys.stdin.read().split()
A = data[0]
B = data[1]

# Make same length by padding with zeros on the left
len_a = len(A)
len_b = len(B)
max_len = max(len_a, len_b)

A_padded = A.zfill(max_len)
B_padded = B.zfill(max_len)

# Process from least significant to most significant (right to left)
# We'll work with lists
a_digits = list(A_padded)
b_digits = list(B_padded)

# For each position from right to left, compare digits
# digit of lesser value is eliminated from its number
a_remaining = []
b_remaining = []

for i in range(max_len - 1, -1, -1):
    da = int(a_digits[i])
    db = int(b_digits[i])
    if da < db:
        # eliminate da from A (don't add to a_remaining)
        b_remaining.append(b_digits[i])
    elif db < da:
        # eliminate db from B
        a_remaining.append(a_digits[i])
    else:
        # equal, neither eliminated
        a_remaining.append(a_digits[i])
        b_remaining.append(b_digits[i])

# Reverse since we processed right to left
a_remaining.reverse()
b_remaining.reverse()

# Convert to numbers
def digits_to_num(digits):
    if not digits:
        return -1
    s = ''.join(digits)
    # Remove leading zeros but keep at least one digit
    val = int(s)
    return val

res_a = digits_to_num(a_remaining)
res_b = digits_to_num(b_remaining)

# Output in non-decreasing order
results = sorted([res_a, res_b])
print(results[0], results[1])