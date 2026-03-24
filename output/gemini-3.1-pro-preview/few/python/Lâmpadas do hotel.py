import sys

input_data = sys.stdin.read().split()
if input_data:
    ia, ib, fa, fb = map(int, input_data[:4])
    if ib == fb:
        print(0 if ia == fa else 1)
    else:
        print(2 if ia == fa else 1)