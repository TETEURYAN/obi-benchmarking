import sys

D = int(sys.stdin.read().split()[0])
remainder = D % 400
print(min(remainder, 400 - remainder))