
N = int(input())
D = int(input())
A = int(input())

if A == D:
    print(0)
elif A < D:
    print(min(D - A, N - (D - A)))
else:
    print(min(A - D, N - (A - D)))
