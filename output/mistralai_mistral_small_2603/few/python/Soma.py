
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return

    n = int(data[0])
    k = int(data[1])
    nums = list(map(int, data[2:2+n]))

    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i+1] = prefix[i] + nums[i]

    count = 0
    freq = {}
    for i in range(n + 1):
        current = prefix[i]
        target = current - k
        if target in freq:
            count += freq[target]
        freq[current] = freq.get(current, 0) + 1

    print(count)

if __name__ == "__main__":
    main()
