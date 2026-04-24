
import sys

def main():
    data = sys.stdin.read().split()
    A = int(data[0])
    S = int(data[1])
    D = int(data[2])

    if A <= S:
        print(1)
        return

    days = 0
    current = 0

    while True:
        days += 1
        current += S
        if current >= A:
            break
        current -= D

    print(days)

if __name__ == "__main__":
    main()
