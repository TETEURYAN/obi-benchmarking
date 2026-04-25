import sys

lista = list(map(int, sys.stdin.read().split()))
pos = [0] * 17
for i in range(16):
    pos[lista[i]] = i + 1
p1 = pos[1]
p9 = pos[9]
if (p1 - 1) // 2 == (p9 - 1) // 2:
    print("oitavas")
elif (p1 - 1) // 4 == (p9 - 1) // 4:
    print("quartas")
elif (p1 <= 8) == (p9 <= 8):
    print("semifinal")
else:
    print("final")