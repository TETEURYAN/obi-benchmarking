
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
A = list(map(int, data[1:]))

if N % 2 == 0:
    mid = N // 2
    s = A[0] + A[N-1]
    is_escher = True
    for i in range(1, mid):
        if A[i] + A[N-1-i] != s:
            is_escher = False
            break
    if is_escher and A[mid-1] + A[mid] == s:
        print("S")
    else:
        print("N")
else:
    mid = N // 2
    s = A[0] + A[N-1]
    is_escher = True
    for i in range(1, mid):
        if A[i] + A[N-1-i] != s:
            is_escher = False
            break
    if is_escher and A[mid] * 2 == s:
        print("S")
    else:
        print("N")
