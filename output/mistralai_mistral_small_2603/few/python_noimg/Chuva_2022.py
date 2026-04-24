
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return

    n = int(data[0])
    s = int(data[1])
    arr = list(map(int, data[2:2+n]))

    prefix_sum = 0
    count = 0
    sum_counts = {0: 1}

    for num in arr:
        prefix_sum += num
        if (prefix_sum - s) in sum_counts:
            count += sum_counts[prefix_sum - s]
        sum_counts[prefix_sum] = sum_counts.get(prefix_sum, 0) + 1

    print(count)

if __name__ == "__main__":
    main()
