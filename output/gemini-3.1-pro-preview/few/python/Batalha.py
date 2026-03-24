import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

a1 = int(input_data[0])
d1 = int(input_data[1])
a2 = int(input_data[2])
d2 = int(input_data[3])

f1 = (d1 != a2)
f2 = (d2 != a1)

if not f1 and f2:
    print(1)
elif not f2 and f1:
    print(2)
else:
    print(-1)