import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

v = int(input_data[0])
p = int(input_data[1])

base = v // p
rem = v % p

for i in range(p):
    if i < rem:
        print(base + 1)
    else:
        print(base)