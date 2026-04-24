
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
B = int(data[1])
arquivos = list(map(int, data[2:]))

arquivos.sort()

pastas = 0
left = 0
right = N - 1

while left <= right:
    if arquivos[left] + arquivos[right] <= B:
        pastas += 1
        left += 1
        right -= 1
    else:
        pastas += 1
        right -= 1

print(pastas)
