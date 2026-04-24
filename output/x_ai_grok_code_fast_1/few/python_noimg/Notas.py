import sys

data = sys.stdin.read().split()
N = int(data[0])
notas = list(map(int, data[1:]))
freq = [0] * 101
for nota in notas:
    freq[nota] += 1
max_freq = max(freq)
maior_nota = -1
for i in range(100, -1, -1):
    if freq[i] == max_freq:
        maior_nota = i
        break
print(maior_nota)