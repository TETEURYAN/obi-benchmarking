import sys

input_data = sys.stdin.read().split()
N = int(input_data[0])
word1 = input_data[1]
M = int(input_data[2])
word2 = input_data[3]

len_prefix = 0
min_len = min(N, M)
for i in range(min_len):
    if word1[i] == word2[i]:
        len_prefix += 1
    else:
        break

print(len_prefix)