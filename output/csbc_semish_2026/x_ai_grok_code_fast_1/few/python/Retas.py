import sys

data = sys.stdin.read().split()
idx = 0
N = int(data[idx]); idx += 1
X1 = int(data[idx]); idx += 1
X2 = int(data[idx]); idx += 1
lines = []
for i in range(N):
    A = int(data[idx]); idx += 1
    B = int(data[idx]); idx += 1
    lines.append((A, B))

if X1 == X2:
    from collections import Counter
    ys = [A * X1 + B for A, B in lines]
    cnt = Counter(ys)
    ans = 0
    for v in cnt.values():
        ans += v * (v - 1) // 2
    print(ans)
else:
    pairs = [(A * X1 + B, A * X2 + B) for A, B in lines]
    pairs.sort(key=lambda x: x[0])
    
    def merge(arr, left, mid, right):
        n1 = mid - left + 1
        n2 = right - mid
        L = [arr[left + i] for i in range(n1)]
        R = [arr[mid + 1 + j] for j in range(n2)]
        i = 0
        j = 0
        k = left
        inv = 0
        while i < n1 and j < n2:
            if L[i][1] <= R[j][1]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
                inv += (n1 - i)
            k += 1
        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1
        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1
        return inv
    
    def merge_sort(arr, left, right):
        inv = 0
        if left < right:
            mid = (left + right) // 2
            inv += merge_sort(arr, left, mid)
            inv += merge_sort(arr, mid + 1, right)
            inv += merge(arr, left, mid, right)
        return inv
    
    ans = merge_sort(pairs, 0, len(pairs) - 1)
    print(ans)