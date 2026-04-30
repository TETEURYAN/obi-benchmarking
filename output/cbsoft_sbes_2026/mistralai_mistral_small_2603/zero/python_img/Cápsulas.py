
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    f = int(data[1])
    cycles = list(map(int, data[2:2+n]))

    low = 1
    high = 10**8
    answer = high

    while low <= high:
        mid = (low + high) // 2
        total = 0
        for c in cycles:
            total += mid // c
            if total >= f:
                break

        if total >= f:
            answer = mid
            high = mid - 1
        else:
            low = mid + 1

    print(answer)

if __name__ == "__main__":
    main()
