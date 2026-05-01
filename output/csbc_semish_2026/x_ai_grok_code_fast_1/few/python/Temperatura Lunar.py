import sys

data = sys.stdin.read().split()
idx = 0
test_num = 1
while True:
    N = int(data[idx])
    M = int(data[idx + 1])
    idx += 2
    if N == 0 and M == 0:
        break
    temps = []
    for i in range(N):
        temps.append(int(data[idx]))
        idx += 1
    prefix = [0]
    for t in temps:
        prefix.append(prefix[-1] + t)
    min_avg = float('inf')
    max_avg = float('-inf')
    for i in range(N - M + 1):
        soma = prefix[i + M] - prefix[i]
        avg = int(soma / M)
        min_avg = min(min_avg, avg)
        max_avg = max(max_avg, avg)
    print(f"Teste {test_num}")
    print(min_avg, max_avg)
    print()
    test_num += 1