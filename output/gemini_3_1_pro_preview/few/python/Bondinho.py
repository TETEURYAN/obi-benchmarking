import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

a = int(input_data[0])
m = int(input_data[1])

if a + m <= 50:
    print("S")
else:
    print("N")