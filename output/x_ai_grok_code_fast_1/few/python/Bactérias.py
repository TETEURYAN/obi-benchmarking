import sys

data = sys.stdin.read().split()
N = int(data[0])
P = int(data[1])

bact = 1
dias = 0
while bact * P <= N:
    bact *= P
    dias += 1

print(dias)