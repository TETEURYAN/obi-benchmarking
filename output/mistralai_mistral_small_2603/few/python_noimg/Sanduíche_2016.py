
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return

    n = int(data[0])
    d = int(data[1])
    c = list(map(int, data[2:2+n]))

    total = 0
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i+1] = prefix[i] + c[i]

    count = 0
    freq = {}
    for i in range(n + 1):
        target = prefix[i] - d
        if target in freq:
            count += freq[target]
        freq[prefix[i]] = freq.get(prefix[i], 0) + 1

    total += count

    left = 0
    right = n - 1
    sum_left = 0
    sum_right = 0
    count_edges = 0

    while left <= right:
        if sum_left + c[left] <= d:
            sum_left += c[left]
            left += 1
        elif sum_right + c[right] <= d:
            sum_right += c[right]
            right -= 1
        else:
            break

        if sum_left == d:
            count_edges += 1
            sum_left -= c[left - 1]
            left -= 1
        if sum_right == d:
            count_edges += 1
            sum_right -= c[right + 1]
            right += 1

    total += count_edges

    print(total)

if __name__ == "__main__":
    main()
