n = int(input())
a = list(map(int, input().split()))

escher = True
s = a[0] + a[n-1]
for i in range(n//2):
    if a[i] + a[n-1-i] != s:
        escher = False
        break

print('S' if escher else 'N')