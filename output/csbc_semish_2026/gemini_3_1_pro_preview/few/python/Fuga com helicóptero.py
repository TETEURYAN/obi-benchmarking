import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

H = int(input_data[0])
P = int(input_data[1])
F = int(input_data[2])
D = int(input_data[3])

while True:
    if F == H:
        print("S")
        break
    if F == P:
        print("N")
        break
    F = (F + D) % 16