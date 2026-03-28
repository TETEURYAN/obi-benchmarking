import sys

input_data = sys.stdin.read().split()
N = int(input_data[0])
K = int(input_data[1])
A = list(map(int, input_data[2:]))
A.sort(reverse=True)
print(A[K-1])