import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
p = [int(x) for x in input_data[1:n+1]]

dark = [p[i] + p[(i + 1) % n] < 1000 for i in range(n)]

if all(dark):
    print(n)
else:
    max_consecutive = 0
    current_consecutive = 0
    
    for d in dark:
        if d:
            current_consecutive += 1
        else:
            if current_consecutive > max_consecutive:
                max_consecutive = current_consecutive
            current_consecutive = 0
            
    for d in dark:
        if d:
            current_consecutive += 1
        else:
            if current_consecutive > max_consecutive:
                max_consecutive = current_consecutive
            current_consecutive = 0
            
    print(max_consecutive)