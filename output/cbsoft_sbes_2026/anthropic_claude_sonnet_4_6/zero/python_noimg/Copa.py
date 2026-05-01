k = int(input())
l = int(input())

def group(pos, size):
    return (pos - 1) // size

g1 = group(k, 2)
g2 = group(l, 2)

if g1 == g2:
    print("oitavas")
elif group(k, 4) == group(l, 4):
    print("quartas")
elif group(k, 8) == group(l, 8):
    print("semifinal")
else:
    print("final")