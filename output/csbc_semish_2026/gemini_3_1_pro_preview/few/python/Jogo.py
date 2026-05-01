import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

x = int(input_data[0])

for i in range(1, len(input_data)):
    t = int(input_data[i])
    if t > x:
        print("menor")
    elif t < x:
        print("maior")
    else:
        print("correto")