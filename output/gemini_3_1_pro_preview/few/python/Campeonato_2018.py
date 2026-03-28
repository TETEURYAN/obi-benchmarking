import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

A = [int(x) for x in input_data]
p1 = A.index(1)
p9 = A.index(9)

if p1 // 2 == p9 // 2:
    print("oitavas")
elif p1 // 4 == p9 // 4:
    print("quartas")
elif p1 // 8 == p9 // 8:
    print("semifinal")
else:
    print("final")