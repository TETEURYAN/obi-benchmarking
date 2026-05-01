
import sys

input = sys.stdin.read
data = input().strip().split()
N = int(data[0])
M = int(data[1])

if N % (M + 1) == 0:
    print("Carlos")
else:
    print("Paula")
