import sys

input_data = sys.stdin.read().split()
A1 = int(input_data[0])
D1 = int(input_data[1])
A2 = int(input_data[2])
D2 = int(input_data[3])

j1_safe = D1 != A2
j2_safe = D2 != A1

if j1_safe and not j2_safe:
    print(1)
elif not j1_safe and j2_safe:
    print(2)
else:
    print(-1)