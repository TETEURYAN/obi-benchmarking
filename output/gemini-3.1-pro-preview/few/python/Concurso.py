import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
k = int(input_data[1])
a = [int(x) for x in input_data[2:2+n]]

a.sort(reverse=True)
print(a[k-1])