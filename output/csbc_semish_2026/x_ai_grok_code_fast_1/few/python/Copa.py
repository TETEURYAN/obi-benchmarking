import sys

K = int(sys.stdin.readline().strip())
L = int(sys.stdin.readline().strip())
a = K - 1
b = L - 1
r = 0
while True:
    if (a // (1 << r)) != (b // (1 << r)):
        break
    r += 1
fases = ["oitavas", "quartas", "semifinal", "final"]
print(fases[r - 1])