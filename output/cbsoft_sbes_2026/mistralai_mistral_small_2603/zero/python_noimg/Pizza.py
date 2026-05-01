
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    arr = list(map(int, data[1:n+1]))

    if n == 0:
        print(0)
        return

    total_sum = sum(arr)
    max_sum = current_sum = 0

    for num in arr:
        current_sum = max(0, current_sum + num)
        max_sum = max(max_sum, current_sum)

    if max_sum == 0:
        print(0)
        return

    if total_sum == max_sum:
        print(max_sum)
        return

    min_sum = current_sum = 0
    for num in arr:
        current_sum = min(0, current_sum + num)
        min_sum = min(min_sum, current_sum)

    circular_max = total_sum - min_sum
    print(max(max_sum, circular_max))

if __name__ == "__main__":
    main()
