import sys

input_data = sys.stdin.read().split()
N = int(input_data[0])
ops = list(map(int, input_data[1:]))

count1 = 0
count2 = 0
for op in ops:
    if op == 1:
        count1 += 1
    else:
        count2 += 1

A = (count1 + count2) % 2
B = count2 % 2

print(A)
print(B)