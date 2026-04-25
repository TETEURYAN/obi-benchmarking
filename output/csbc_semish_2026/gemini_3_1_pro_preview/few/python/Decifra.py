import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

perm = input_data[0]
encrypted = input_data[1]

decrypted = "".join(perm[ord(ch) - ord('a')] for ch in encrypted)
print(decrypted)