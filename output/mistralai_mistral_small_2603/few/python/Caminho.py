
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return

    n = int(data[0])
    powers = list(map(int, data[1:n+1]))

    max_dark = 0
    current = 0

    for i in range(n):
        next_i = (i + 1) % n
        if powers[i] + powers[next_i] < 1000:
            current += 1
            if current > max_dark:
                max_dark = current
        else:
            current = 0

    print(max_dark)

if __name__ == "__main__":
    main()
