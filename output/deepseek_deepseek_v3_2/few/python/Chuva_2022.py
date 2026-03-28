import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    S = int(next(it))
    arr = [int(next(it)) for _ in range(N)]

    prefix_sum = 0
    count_map = {0: 1}
    result = 0

    for x in arr:
        prefix_sum += x
        target = prefix_sum - S
        result += count_map.get(target, 0)
        count_map[prefix_sum] = count_map.get(prefix_sum, 0) + 1

    print(result)

if __name__ == "__main__":
    main()