import sys

input_data = sys.stdin.read().splitlines()
perm = input_data[0]
cipher = input_data[1]

inv_map = {}
for i in range(26):
    original = chr(ord('a') + i)
    encrypted = perm[i]
    inv_map[encrypted] = original

result = ''.join(inv_map[c] for c in cipher)
print(result)