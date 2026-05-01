import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
b = int(input_data[1])
files = [int(x) for x in input_data[2:2+n]]

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
        folders += 1
    else:
        right -= 1
        folders += 1

print(folders)