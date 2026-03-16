import sys

def count_inversions(arr):
    n = len(arr)
    if n <= 1:
        return 0
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
    lines = []
    for idx in range(N):
        A, B = map(int, input().split())
        y1 = A * X1 + B
        y2 = A * X2 + B
        lines.append((y1, y2, idx))

    lines.sort(key=lambda x: (x[0], x[1]))
    arr = [y2 for y1, y2, idx in lines]
    print(count_inversions(arr))

if __name__ == "__main__":
    main()
