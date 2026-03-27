import sys

input_data = sys.stdin.read().split()
A = int(input_data[0])
S = int(input_data[1])
D = int(input_data[2])
diff = S - D
num = A - D
n = (num + diff - 1) // diff
print(max(1, n))