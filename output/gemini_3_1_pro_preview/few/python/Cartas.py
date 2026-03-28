import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

a = int(input_data[0])
b = int(input_data[1])
c = int(input_data[2])

if a == b:
    print(c)
elif a == c:
    print(b)
else:
    print(a)