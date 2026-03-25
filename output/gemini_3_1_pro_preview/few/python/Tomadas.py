import sys

input_data = sys.stdin.read().split()
if len(input_data) >= 4:
    t1, t2, t3, t4 = map(int, input_data[:4])
    print(t1 + t2 + t3 + t4 - 3)