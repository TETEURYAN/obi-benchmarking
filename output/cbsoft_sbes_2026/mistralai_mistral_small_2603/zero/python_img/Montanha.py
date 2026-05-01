n=int(input())
a=list(map(int,input().split()))
s='N'
for i in range(1,n-1):
 if a[i-1]>a[i] and a[i]<a[i+1]:
  s='S'
  break
print(s)