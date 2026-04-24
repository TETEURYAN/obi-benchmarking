import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    A = list(map(int, data[1:1+n]))

    left_max = [0] * n
    right_max = [0] * n

    for i in range(n):
        left_max[i] = A[i] + i

    for i in range(n):
        right_max[i] = A[i] + (n - 1 - i)

    prefix_left = [0] * n
    suffix_right = [0] * n

    prefix_left[0] = left_max[0]
    for i in range(1, n):
        prefix_left[i] = max(prefix_left[i-1], left_max[i])

    suffix_right[-1] = right_max[-1]
    for i in range(n-2, -1, -1):
        suffix_right[i] = max(suffix_right[i+1], right_max[i])

    ans = 0
    for i in range(n):
        candidate = prefix_left[i] + suffix_right[i]
        ans = max(ans, candidate)

    print(ans)

if __name__ == "__main__":
    main()