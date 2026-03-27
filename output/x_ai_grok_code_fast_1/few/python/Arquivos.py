import sys

input_data = sys.stdin.read().split()

N = int(input_data[0])
B = int(input_data[1])
sizes = list(map(int, input_data[2:]))

sizes.sort()

i = 0
j = N - 1
pastas = 0

while i <= j:
    if i == j:
        pastas += 1
        i += 1
    elif sizes[i] + sizes[j] <= B:
        pastas += 1
        i += 1
        j -= 1
    else:
        pastas += 1
        j -= 1

print(pastas)