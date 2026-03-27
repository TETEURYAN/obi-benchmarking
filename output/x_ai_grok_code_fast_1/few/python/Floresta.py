import sys

data = sys.stdin.read().split()
N = int(data[0])

count = 0
max_x = 10**5 + 10  # sufficient for N=1e9
for x in range(2, max_x):
    denom = 2 * x - 1
    num = N - 1 + x
    if num % denom == 0:
        y = num // denom
        if y >= x:
            count += 1

print(count)