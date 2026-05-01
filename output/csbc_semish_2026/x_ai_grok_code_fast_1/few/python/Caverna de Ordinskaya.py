import sys

input_data = sys.stdin.read().split()
N = int(input_data[0])
M = int(input_data[1])
A = list(map(int, input_data[2:]))

last = 0
soma = 0
for a in A:
    opt1 = a
    opt2 = M - a
    small = min(opt1, opt2)
    large = max(opt1, opt2)
    if small >= last:
        choose = small
    elif large >= last:
        choose = large
    else:
        print(-1)
        sys.exit(0)
    soma += choose
    last = choose

print(soma)