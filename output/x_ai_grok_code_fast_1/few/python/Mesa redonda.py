import sys

data = sys.stdin.read().split()
A = int(data[0])
B = int(data[1])

cadeira_Ana = (1 + (A - 1)) % 3
ocupadas = set([cadeira_Ana])

cadeira_Beatriz_tent = (1 + (B - 1)) % 3
if cadeira_Beatriz_tent not in ocupadas:
    cadeira_Beatriz = cadeira_Beatriz_tent
else:
    cadeira_Beatriz = (cadeira_Beatriz_tent + 1) % 3
ocupadas.add(cadeira_Beatriz)

for i in range(3):
    if i not in ocupadas:
        print(i)
        break