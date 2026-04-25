import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
dario = 0
xerxes = 0

idx = 1
for _ in range(n):
    d = int(input_data[idx])
    x = int(input_data[idx+1])
    idx += 2
    
    if (x - d) % 5 in (1, 2):
        dario += 1
    else:
        xerxes += 1

if dario > xerxes:
    print("dario")
else:
    print("xerxes")