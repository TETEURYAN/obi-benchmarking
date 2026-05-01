import sys

data = list(map(int, sys.stdin.read().split()))
if data:
    n = data[0]
    divisoes = data[1:1+n]
    print(sum(x - 1 for x in divisoes))