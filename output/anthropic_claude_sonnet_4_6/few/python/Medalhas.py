import sys

data = sys.stdin.read().split()
t1, t2, t3 = int(data[0]), int(data[1]), int(data[2])

swimmers = [(t1, 1), (t2, 2), (t3, 3)]
swimmers.sort()

print(swimmers[0][1])
print(swimmers[1][1])
print(swimmers[2][1])