import sys
data = sys.stdin.read().split()
n = int(data[0])
registros = set(data[1:n+1])
print(len(registros))