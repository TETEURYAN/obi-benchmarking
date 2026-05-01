import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return

    n = data[0]
    a = data[1:1+n]

    total = sum(a)
    base_sum = n * (n - 1) // 2

    if total < base_sum or (total - base_sum) % n != 0:
        print(-1)
        return

    x = (total - base_sum) // n
    moved = 0
    for i in range(n):
        target = x + i
        if a[i] > target:
            moved += a[i] - target

    print(moved)

if __name__ == "__main__":
    main()
