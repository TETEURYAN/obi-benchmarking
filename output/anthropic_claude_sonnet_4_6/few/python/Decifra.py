import sys

data = sys.stdin.read().split()
perm = data[0]
phrase = data[1]

# Build inverse permutation: for each letter in perm, map it back to original
inverse = [''] * 26
for i, c in enumerate(perm):
    inverse[ord(c) - ord('a')] = chr(ord('a') + i)

result = []
for c in phrase:
    result.append(inverse[ord(c) - ord('a')])

print(''.join(result))