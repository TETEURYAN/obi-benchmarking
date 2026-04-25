import sys

data = sys.stdin.read().split()
N = int(data[0])
index = 1
max_lats = []
Cs = []
Fs = []
for i in range(N):
    A = int(data[index])
    B = int(data[index + 1])
    C = int(data[index + 2])
    D = int(data[index + 3])
    E = int(data[index + 4])
    F = int(data[index + 5])
    max_lat = max(B, C, D, F)
    max_lats.append(max_lat)
    Cs.append(C)
    Fs.append(F)
    index += 6
total_sum = sum(max_lats)
given_valid = True
for i in range(1, N):
    if Fs[i] != Cs[i - 1]:
        given_valid = False
        break
given_score = total_sum if given_valid else 0
any_score = total_sum
print(max(given_score, any_score))