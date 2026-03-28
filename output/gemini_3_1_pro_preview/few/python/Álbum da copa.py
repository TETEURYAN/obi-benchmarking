import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
m = int(input_data[1])

stickers = set()
for i in range(2, 2 + m):
    stickers.add(int(input_data[i]))

print(n - len(stickers))