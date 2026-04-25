import sys
data = sys.stdin.read().split()
a = set(data[:6])
b = set(data[6:])
hits = len(a & b)
if hits == 6:
    print("sena")
elif hits == 5:
    print("quina")
elif hits == 4:
    print("quadra")
elif hits == 3:
    print("terno")
else:
    print("azar")