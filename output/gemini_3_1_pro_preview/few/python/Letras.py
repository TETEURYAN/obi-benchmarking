import sys
from bisect import bisect_right

input_data = sys.stdin.read().split()
if not input_data:
    exit()

s = input_data[0]
tails = []

for char in s:
    pos = bisect_right(tails, char)
    if pos == len(tails):
        tails.append(char)
    else:
        tails[pos] = char

print(len(tails))