
import sys

def main():
    input = sys.stdin.read().split()
    ptr = 0
    N, F = map(int, input[ptr:ptr+2])
    ptr += 2
    C = list(map(int, input[ptr:ptr+N]))

    left = 1
    right = 10**8
    answer = right

    while left <= right:
        mid = (left + right) // 2
        total = 0
        for c in C:
            total += mid // c
            if total >= F:
                break
        if total >= F:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    print(answer)

if __name__ == "__main__":
    main()
