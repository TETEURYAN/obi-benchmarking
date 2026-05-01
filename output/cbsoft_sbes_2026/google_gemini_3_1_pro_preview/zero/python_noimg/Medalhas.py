import sys

t1 = int(sys.stdin.readline())
t2 = int(sys.stdin.readline())
t3 = int(sys.stdin.readline())

times = [(t1, 1), (t2, 2), (t3, 3)]
times.sort()

for time, swimmer in times:
    print(swimmer)