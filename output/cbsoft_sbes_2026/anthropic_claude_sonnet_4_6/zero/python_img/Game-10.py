N = int(input())
D = int(input())
A = int(input())

if A == D:
    print(0)
elif D > A:
    print(D - A)
else:
    print(N - A + D)