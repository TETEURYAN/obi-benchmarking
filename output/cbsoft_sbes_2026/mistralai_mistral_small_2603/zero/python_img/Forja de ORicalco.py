
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
    left = 0
    for right in range(n):
        current_or |= a[right]
        if right - left + 1 == k:
            segment_or = current_or
            remaining_sum = total - sum(a[left:right+1])
            candidate = remaining_sum + segment_or
            if candidate < min_impurity:
                min_impurity = candidate
            current_or ^= a[left]
            left += 1

    print(min_impurity)

if __name__ == "__main__":
    main()
