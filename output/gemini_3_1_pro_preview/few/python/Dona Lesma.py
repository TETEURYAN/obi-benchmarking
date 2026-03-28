import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

A = int(input_data[0])
S = int(input_data[1])
D = int(input_data[2])

if A <= S:
    print(1)
else:
    days = (A - S + (S - D) - 1) // (S - D) + 1
    print(days)