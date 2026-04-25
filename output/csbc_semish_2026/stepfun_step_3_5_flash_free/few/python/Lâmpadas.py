import sys

data = sys.stdin.read().split()
n = int(data[0])
ops = data[1:1+n]
count1 = ops.count('1')
count2 = n - count1
a = (count1 + count2) % 2
b = count2 % 2
print(a)
print(b)