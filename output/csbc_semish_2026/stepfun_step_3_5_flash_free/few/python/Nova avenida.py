import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    values = list(map(int, data[2:]))
    col_sums = [0] * m
    idx = 0
    for i in range(n):
        for j in range(m):
            col_sums[j] += values[idx]
            idx += 1
    print(min(col_sums))

if __name__ == "__main__":
    main()