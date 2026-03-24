import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
a = int(input_data[1])
b = int(input_data[2])
c = int(input_data[3])
d = int(input_data[4])
e = int(input_data[5])
f = int(input_data[6])
g = int(input_data[7])

if a + b + c - d - e - f == n - g:
    print("N")
else:
    print("S")