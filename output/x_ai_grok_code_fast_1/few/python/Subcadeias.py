import sys

input_data = sys.stdin.read().split()
N = int(input_data[0])
S = input_data[1]

def expand(left, right):
    while left >= 0 and right < len(S) and S[left] == S[right]:
        left -= 1
        right += 1
    return right - left - 1

max_len = 1
for i in range(N):
    # Odd length
    len1 = expand(i, i)
    # Even length
    len2 = expand(i, i + 1)
    max_len = max(max_len, len1, len2)

print(max_len)