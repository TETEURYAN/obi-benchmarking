import sys

input_data = sys.stdin.read().split()
N = int(input_data[0])
L = list(map(int, input_data[1:]))

P = sum(L)
if P % 4 != 0:
    print('N')
else:
    target = P // 4
    cum = [0]
    for l in L:
        cum.append(cum[-1] + l)
    s = set(cum)
    if target in s and 2 * target in s and 3 * target in s:
        print('S')
    else:
        print('N')