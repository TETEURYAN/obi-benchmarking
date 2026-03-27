
import sys

def main():
    data = sys.stdin.read().split()
    N = int(data[0])
    R = int(data[1])
    P = int(data[2])

    total = N
    days = 0

    while total < P:
        new_infections = N * (R ** days)
        total += new_infections
        days += 1

    print(days)

if __name__ == "__main__":
    main()
