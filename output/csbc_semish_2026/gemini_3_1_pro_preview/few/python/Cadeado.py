import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
ans = 0
idx = 1

for _ in range(n):
    c = int(input_data[idx])
    s = int(input_data[idx+1])
    idx += 2
    
    diff = abs(c - s)
    ans += min(diff, 10 - diff)

print(ans)