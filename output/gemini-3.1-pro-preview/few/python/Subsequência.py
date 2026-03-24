import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

A = int(input_data[0])
B = int(input_data[1])

SA = input_data[2 : 2 + A]
SB = input_data[2 + A : 2 + A + B]

i = 0
j = 0
while i < A and j < B:
    if SA[i] == SB[j]:
        j += 1
    i += 1

if j == B:
    print('S')
else:
    print('N')