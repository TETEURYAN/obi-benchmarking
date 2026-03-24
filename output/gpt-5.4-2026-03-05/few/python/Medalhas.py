import sys

data = sys.stdin.read().split()
t1, t2, t3 = map(int, data[:3])

tempos = [(t1, 1), (t2, 2), (t3, 3)]
tempos.sort()

print(tempos[0][1])
print(tempos[1][1])
print(tempos[2][1])