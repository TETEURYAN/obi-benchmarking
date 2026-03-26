import sys

data = sys.stdin.read().split()
n = int(data[0])
switches = data[1:n+1]

count1 = switches.count('1')
count2 = switches.count('2')

a = (count1 + count2) % 2
b = count2 % 2

print(a)
print(b)