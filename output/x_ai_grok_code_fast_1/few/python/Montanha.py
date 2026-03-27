import sys

input_data = sys.stdin.read().split()
N = int(input_data[0])
A = list(map(int, input_data[1:]))

has_multiple_peaks = False
for i in range(1, N-1):
    if A[i-1] > A[i] and A[i] < A[i+1]:
        has_multiple_peaks = True
        break

if has_multiple_peaks:
    print("S")
else:
    print("N")