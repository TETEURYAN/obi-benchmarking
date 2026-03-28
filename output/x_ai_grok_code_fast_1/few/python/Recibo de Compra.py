import sys

def count_combinations(current_sum, last, count, R, K):
    if count == K:
        return 1 if current_sum == R else 0
    total = 0
    for i in range(last + 1, R - current_sum + 1):
        total += count_combinations(current_sum + i, i, count + 1, R, K)
    return total

input_data = sys.stdin.read().split()
R = int(input_data[0])
K = int(input_data[1])

result = count_combinations(0, 0, 0, R, K)
print(result)