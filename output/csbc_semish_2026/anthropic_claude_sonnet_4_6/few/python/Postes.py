import sys

data = sys.stdin.read().split()
n = int(data[0])
postes = list(map(int, data[1:n+1]))

substituir = sum(1 for x in postes if x < 50)
consertar = sum(1 for x in postes if 50 <= x < 85)

print(substituir, consertar)