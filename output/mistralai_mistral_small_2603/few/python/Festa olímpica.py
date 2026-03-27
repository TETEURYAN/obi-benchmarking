
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    N = int(data[0])
    M = int(data[1])
    T = list(map(int, data[2:2+M]))

    if M == 0:
        if N <= 10000:
            for i in range(1, N+1):
                print(i)
        else:
            for i in range(1, 10001):
                print(i)
        return

    current = 1
    step = 1
    for t in T:
        if t <= current:
            step = step * t // (t - 1)
        else:
            step = step * t

    remaining = N // step
    if remaining <= 10000:
        for i in range(1, remaining + 1):
            print(i * step)
    else:
        for i in range(1, 10001):
            print(i * step)

if __name__ == "__main__":
    main()
