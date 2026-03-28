import sys

data = sys.stdin.read().split()
n = int(data[0])
if n == 1:
    print(1)
else:
    seq = list(map(int, data[1:n+1]))
    count = 1
    i = 0
    while i < n - 1:
        diff = seq[i+1] - seq[i]
        j = i + 1
        while j < n - 1 and seq[j+1] - seq[j] == diff:
            j += 1
        count += 1
        i = j
    print(count)