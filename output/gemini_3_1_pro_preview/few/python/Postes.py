import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
substituidos = 0
consertados = 0

for i in range(1, n + 1):
    h = int(input_data[i])
    if h < 50:
        substituidos += 1
    elif h < 85:
        consertados += 1

print(f"{substituidos} {consertados}")