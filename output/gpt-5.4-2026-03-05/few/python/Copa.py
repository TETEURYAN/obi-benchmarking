import sys

data = sys.stdin.read().split()
k = int(data[0])
l = int(data[1])

while k != l:
    k = (k + 1) // 2
    l = (l + 1) // 2

if k <= 8:
    print("oitavas")
elif k <= 4:
    print("quartas")
elif k <= 2:
    print("semifinal")
else:
    print("final")