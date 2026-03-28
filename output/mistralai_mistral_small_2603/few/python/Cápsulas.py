
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    f = int(data[1])
    cycles = list(map(int, data[2:2+n]))

    left = 1
    right = 10**8
    answer = right

    while left <= right:
        mid = (left + right) // 2
        total = 0
        for c in cycles:
            total += mid // c
            if total >= f:
                break
        if total >= f:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    print(answer)

if __name__ == "__main__":
    main()
