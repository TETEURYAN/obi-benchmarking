import sys

sys.setrecursionlimit(200000)

def solve():
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    n = int(input_data[0])
    
    if n == 0:
        print(0)
        return

    arr = list(map(int, input_data[1:n+1]))
    
    temp = [0] * n
    
    def merge_sort_count(left, right):
        if left >= right:
            return 0
        
        mid = (left + right) // 2
        
        inv_count = merge_sort_count(left, mid)
        inv_count += merge_sort_count(mid + 1, right)
        inv_count += merge(left, mid, right)
        
        return inv_count

    def merge(left, mid, right):
        i = left
        j = mid + 1
        k = left
        inv_count = 0
        
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp[k] = arr[i]
                i += 1
            else:
                temp[k] = arr[j]
                inv_count += (mid - i + 1)
                j += 1
            k += 1
            
        while i <= mid:
            temp[k] = arr[i]
            i += 1
            k += 1
            
        while j <= right:
            temp[k] = arr[j]
            j += 1
            k += 1
            
        for idx in range(left, right + 1):
            arr[idx] = temp[idx]
            
        return inv_count

    result = merge_sort_count(0, n - 1)
    print(result)

if __name__ == "__main__":
    solve()