
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
index = 1
total = 0

for i in range(N):
    c = int(data[index])
    s = int(data[index + 1])
    index += 2
    diff = abs(c - s)
    min_clicks = min(diff, 10 - diff)
    total += min_clicks

print(total)
