import sys

def main():
    data = sys.stdin.read().split()
    N = int(data[0])
    M = int(data[1])

    if M == 0:
        print(0)
        return

    g = 1
    for i in range(1, int(min(N, M)**0.5) + 1):
        if N % i == 0 and M % i == 0:
            g = i

    max_x = 0
    for k in range(1, int(min(N, M)**0.5) + 1):
        if N % k == 0:
            candidate = N // k - 1
            if candidate <= M and candidate > max_x:
                max_x = candidate
        if M % k == 0:
            candidate = M // k - 1
            if candidate <= M and candidate > max_x:
                max_x = candidate

    print(max_x)

if __name__ == "__main__":
    main()