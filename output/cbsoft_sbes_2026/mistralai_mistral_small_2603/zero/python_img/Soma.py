
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    k = int(data[1])
    arr = list(map(int, data[2:2+n]))

    prefix = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix[i] = prefix[i-1] + arr[i-1]

    count = 0
    freq = {}
    for i in range(n + 1):
        current = prefix[i]
        if current == k:
            count += 1
        if (current - k) in freq:
            count += freq[current - k]
        freq[current] = freq.get(current, 0) + 1

    print(count)

if __name__ == "__main__":
    main()
