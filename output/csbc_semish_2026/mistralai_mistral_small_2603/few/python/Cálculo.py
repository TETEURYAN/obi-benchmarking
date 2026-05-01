
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    idx = 0
    M = int(data[idx])
    N = int(data[idx + 1])
    idx += 2

    X = list(map(int, data[idx:idx + M]))
    idx += M
    Y = list(map(int, data[idx:idx + N]))

    carry = 0
    result = []
    max_len = max(M, N)

    for i in range(max_len):
        bit_x = X[i] if i < M else 0
        bit_y = Y[i] if i < N else 0
        total = bit_x + bit_y + carry
        if total == 0:
            result.append(0)
            carry = 0
        elif total == 1:
            result.append(1)
            carry = 0
        elif total == 2:
            result.append(0)
            carry = 1
        else:  # total == 3
            result.append(1)
            carry = 1

    if carry:
        result.append(carry)

    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()
