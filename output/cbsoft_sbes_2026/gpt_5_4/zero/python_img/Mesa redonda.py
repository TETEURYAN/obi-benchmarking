import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())

ana = A % 3
beatriz = B % 3
if beatriz == ana:
    beatriz = (beatriz + 1) % 3

carolina = 3 - ana - beatriz
print(carolina)