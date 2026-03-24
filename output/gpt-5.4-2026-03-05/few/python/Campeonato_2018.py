import sys

a = list(map(int, sys.stdin.read().split()))

p1 = a.index(1) + 1
p9 = a.index(9) + 1

if (p1 - 1) // 2 == (p9 - 1) // 2:
    print("oitavas")
elif (p1 - 1) // 4 == (p9 - 1) // 4:
    print("quartas")
elif (p1 - 1) // 8 == (p9 - 1) // 8:
    print("semifinal")
else:
    print("final")