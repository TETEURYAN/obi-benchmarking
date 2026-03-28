import sys

data = sys.stdin.read().split()
A = int(data[0])
B = int(data[1])

ana = A % 3
beatriz = B % 3

if beatriz == ana:
    beatriz = (beatriz + 1) % 3

carolina = 3 - ana - beatriz

print(carolina)