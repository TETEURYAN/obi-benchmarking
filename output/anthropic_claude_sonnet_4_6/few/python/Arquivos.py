import sys

data = sys.stdin.read().split()
n = int(data[0])
b = int(data[1])
files = [int(data[i+2]) for i in range(n)]

files.sort()

left = 0
right = n - 1
folders = 0

while left <= right:
    if left == right:
        folders += 1
        break
    if files[left] + files[right] <= b:
        left += 1
        right -= 1
    else:
        right -= 1
    folders += 1

print(folders)