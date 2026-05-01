n = int(input())
a = list(map(int, input().split()))
target = a[0] + a[-1]
escher = all(a[i] + a[n-1-i] == target for i in range(n))
print('S' if escher else 'N')