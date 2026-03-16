import sys

def count_inversions(arr):
    n = len(arr)
    temp = [0] * n

    def sort_count(l, r):
        if r - l <= 1:
            return 0
        m = (l + r) // 2
        inv = sort_count(l, m) + sort_count(m, r)
        i, j, k = l, m, l
        while i < m and j < r:
            if arr[i] <= arr[j]:
                temp[k] = arr[i]
                i += 1
            else:
                temp[k] = arr[j]
                inv += m - i
                j += 1
            k += 1
        while i < m:
            temp[k] = arr[i]
            i += 1
            k += 1
        while j < r:
            temp[k] = arr[j]
            j += 1
            k += 1
        arr[l:r] = temp[l:r]
        return inv

    return sort_count(0, n)

def main():
    input = sys.stdin.readline
    N, X1, X2 = map(int, input().split())
    lines = [tuple(map(int, input().split())) for _ in range(N)]

    vals = []
    for idx, (a, b) in enumerate(lines):
        y1 = a * X1 + b
        y2 = a * X2 + b
        vals.append((y1, y2, idx))

    vals.sort(key=lambda t: (t[0], t[1], t[2]))
    arr = [t[1] for t in vals]
    print(count_inversions(arr))

if __name__ == "__main__":
    main()
