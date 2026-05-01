import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    m, n = data[0], data[1]
    balance = [0] * (n + 1)
    total = 0

    idx = 2
    for _ in range(m):
        x = data[idx]
        v = data[idx + 1]
        y = data[idx + 2]
        idx += 3
        balance[x] -= v
        balance[y] += v
        total += v

    positive_sum = 0
    for i in range(1, n + 1):
        if balance[i] > 0:
            positive_sum += balance[i]

    if positive_sum < total:
        sys.stdout.write("S\n" + str(positive_sum) + "\n")
    else:
        sys.stdout.write("N\n" + str(positive_sum) + "\n")

if __name__ == "__main__":
    main()
