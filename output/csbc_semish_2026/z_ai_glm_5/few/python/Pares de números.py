import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
min_sum = int(input_data[1])
max_sum = int(input_data[2])
vector = list(map(int, input_data[3:]))

count = 0

# Complexidade O(N^2)
# Dado que N <= 1000, o pior caso é 1.000.000 de iterações, o que é rápido o suficiente.
for i in range(n):
    for j in range(i + 1, n):
        s = vector[i] + vector[j]
        if min_sum <= s <= max_sum:
            count += 1

print(count)