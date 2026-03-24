import sys

data = sys.stdin.read().split()
A = int(data[0])
B = int(data[1])

ana = A % 3
bea = B % 3

if bea == ana:
    bea = (bea + 1) % 3

carolina = 3 - ana - bea
print(carolina)