n = int(input())
x = list(map(int, input().split()))
h = max(x)
for row in range(h, 0, -1):
    print(' '.join('1' if x[i] >= row else '0' for i in range(n)))