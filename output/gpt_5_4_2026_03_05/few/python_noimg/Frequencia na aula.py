import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()

n = int(data[0])
presentes = set()

for i in range(1, n + 1):
    presentes.add(int(data[i]))

print(len(presentes))