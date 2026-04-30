a = input().strip()
b = input().strip()

# Make same length by padding with zeros on the left
max_len = max(len(a), len(b))
a_padded = a.zfill(max_len)
b_padded = b.zfill(max_len)

# Process from least significant to most significant (right to left)
a_remaining = list(a_padded)
b_remaining = list(b_padded)

for i in range(max_len - 1, -1, -1):
    da = int(a_padded[i])
    db = int(b_padded[i])
    if da < db:
        a_remaining[i] = None
    elif db < da:
        b_remaining[i] = None
    # if equal, neither is eliminated

# Build result numbers from remaining digits
a_digits = ''.join(d for d in a_remaining if d is not None)
b_digits = ''.join(d for d in b_remaining if d is not None)

# Convert to integers (removing leading zeros)
if a_digits == '':
    a_result = -1
else:
    a_result = int(a_digits)

if b_digits == '':
    b_result = -1
else:
    b_result = int(b_digits)

# Output in non-decreasing order
results = sorted([a_result, b_result])
print(results[0], results[1])