import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])

if n == 1:
    print(1)
elif n == 2:
    print(-1)
else:
    c = [i for i in range(1, n)]
    c.append(n * (n - 1) // 2)
    
    for i in range(n):
        r_i = c[-1] * (c[i] - 1)
        row = [r_i + c[j] for j in range(n)]
        print(*(row))