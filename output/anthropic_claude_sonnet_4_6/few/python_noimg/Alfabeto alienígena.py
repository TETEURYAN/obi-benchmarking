import sys

data = sys.stdin.read().split('\n')
first_line = data[0].split()
K, N = int(first_line[0]), int(first_line[1])
alphabet = set(data[1].strip())
message = data[2].strip()

for c in message:
    if c not in alphabet:
        print('N')
        exit()
print('S')