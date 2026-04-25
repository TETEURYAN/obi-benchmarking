import sys

def sum_digits(x):
    return sum(int(d) for d in str(x))

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    N = int(data[0])
    M = int(data[1])
    S = int(data[2])

    ans = -1
    for i in range(M, N - 1, -1):
        if sum_digits(i) == S:
            ans = i
            break
    print(ans)

if __name__ == "__main__":
    main()