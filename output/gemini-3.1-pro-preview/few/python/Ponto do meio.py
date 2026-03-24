import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
ans = (2**n + 1)**2
print(ans)