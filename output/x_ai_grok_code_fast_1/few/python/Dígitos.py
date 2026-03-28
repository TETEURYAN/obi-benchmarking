import sys

data = sys.stdin.read().split()
N = int(data[0])
digits = list(map(int, data[1:]))

min_A = float('inf')
for L in range(1, N + 1):
    A_str = ''.join(map(str, digits[:L]))
    if A_str[0] == '0' and L > 1:
        continue
    A = int(A_str)
    pos = L
    current = A
    success = True
    while pos < N:
        next_num = current + 1
        next_digits = list(str(next_num))
        len_next = len(next_digits)
        if pos + len_next > N:
            success = False
            break
        if digits[pos:pos + len_next] != [int(d) for d in next_digits]:
            success = False
            break
        pos += len_next
        current = next_num
    if success and pos == N:
        if A < min_A:
            min_A = A

print(min_A)