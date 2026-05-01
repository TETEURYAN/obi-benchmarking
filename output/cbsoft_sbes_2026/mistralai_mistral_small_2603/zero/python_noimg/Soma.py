
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    k = int(data[1])
    arr = list(map(int, data[2:2+n]))

    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i+1] = prefix[i] + arr[i]

    count = 0
    freq = {0: 1}

    for i in range(1, n+1):
        current_sum = prefix[i]
        target = current_sum - k
        if target in freq:
            count += freq[target]
        freq[current_sum] = freq.get(current_sum, 0) + 1

    print(count)

if __name__ == "__main__":
    main()
