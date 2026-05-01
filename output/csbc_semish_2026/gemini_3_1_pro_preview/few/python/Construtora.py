import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
a = [int(x) for x in input_data[1:n+1]]

ops = 0
while True:
    min_a = min(a)
    max_a = max(a)
    if min_a == max_a:
        break
    
    i = 0
    while i < n:
        if a[i] == min_a:
            ops += 1
            while i < n and a[i] == min_a:
                a[i] += 1
                i += 1
        else:
            i += 1

print(ops)