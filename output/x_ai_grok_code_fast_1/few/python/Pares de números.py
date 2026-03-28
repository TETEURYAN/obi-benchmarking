import sys

input_data = sys.stdin.read().split()
N = int(input_data[0])
I = int(input_data[1])
F = int(input_data[2])
vetor = [int(x) for x in input_data[3:]]
count = 0
for i in range(N):
    for j in range(i + 1, N):
        soma = vetor[i] + vetor[j]
        if I <= soma <= F:
            count += 1
print(count)