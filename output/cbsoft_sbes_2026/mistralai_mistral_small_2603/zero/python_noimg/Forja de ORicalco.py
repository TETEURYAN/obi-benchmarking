
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    k = int(data[1])
    a = list(map(int, data[2:2+n]))

    if k == 1:
        print(sum(a))
        return

    total = sum(a)
    min_impurity = total

    current_or = 0
    for i in range(k):
        current_or |= a[i]

    window_or = current_or
    for i in range(k, n):
        left = a[i - k]
        right = a[i]
        window_or = window_or | right
        if (window_or & left) == left:
            window_or ^= left
        current_or = window_or
        if current_or < min_impurity:
            min_impurity = current_or

    print(min_impurity)

if __name__ == "__main__":
    main()
