import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
a = [int(x) for x in input_data[1:n+1]]

ops = 0
while True:
    min_val = min(a)
    max_val = max(a)
    if min_val == max_val:
        break
    
    i = 0
    while i < n:
        if a[i] == min_val:
            j = i
            while j < n and a[j] == min_val:
                a[j] += 1
                j += 1
            ops += 1
            i = j
        else:
            i += 1

print(ops)