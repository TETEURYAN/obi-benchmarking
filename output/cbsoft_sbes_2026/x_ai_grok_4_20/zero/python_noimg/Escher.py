
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
A = list(map(int, data[1:]))

if N % 2 == 1:
    mid = N // 2
    target = A[0] + A[N-1]
    is_escher = True
    for i in range(1, mid + 1):
        if A[i] + A[N-1-i] != target:
            is_escher = False
            break
    if is_escher and A[mid] * 2 != target:
        is_escher = False
else:
    target = A[0] + A[N-1]
    is_escher = True
    for i in range(1, N//2):
        if A[i] + A[N-1-i] != target:
            is_escher = False
            break

print("S" if is_escher else "N")
