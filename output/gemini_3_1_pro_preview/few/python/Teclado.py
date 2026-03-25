import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

N = input_data[0]
M = int(input_data[1])
strings = input_data[2:]

trans = str.maketrans("abcdefghijklmnopqrstuvwxyz", "22233344455566677778889999")

count = 0
len_N = len(N)

for s in strings:
    if len(s) == len_N and s.translate(trans) == N:
        count += 1

print(count)