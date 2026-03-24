import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])

p2 = p3 = p5 = p7 = 0

it = iter(input_data[1:])
for d_str, op in zip(it, it):
    sign = 1 if op == '*' else -1
    d = int(d_str)
    
    if d == 2:
        p2 += sign
    elif d == 3:
        p3 += sign
    elif d == 4:
        p2 += sign + sign
    elif d == 5:
        p5 += sign
    elif d == 6:
        p2 += sign
        p3 += sign
    elif d == 7:
        p7 += sign
    elif d == 8:
        p2 += sign * 3
    elif d == 9:
        p3 += sign + sign

res = (1 << p2) * (3 ** p3) * (5 ** p5) * (7 ** p7)
print(res)