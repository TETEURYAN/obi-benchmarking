
import sys

def main():
    data = sys.stdin.read().split()
    N = int(data[0])
    P = int(data[1])
    days = 0
    current = 1
    while current <= N:
        current *= P
        days += 1
    print(days - 1)

if __name__ == "__main__":
    main()
