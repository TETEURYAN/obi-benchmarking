
import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    I = int(data[1])
    F = int(data[2])
    arr = list(map(int, data[3:3+n]))
    arr.sort()
    count = 0
    for i in range(n):
        a = arr[i]
        # Para cada a, queremos encontrar j > i tal que a + arr[j] >= I e a + arr[j] <= F
        # Isso é equivalente a arr[j] >= I - a e arr[j] <= F - a
        left = I - a
        right = F - a
        # Busca binária para encontrar o primeiro índice j > i com arr[j] >= left
        low = i + 1
        high = n - 1
        first_valid = -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] >= left:
                first_valid = mid
                high = mid - 1
            else:
                low = mid + 1
        if first_valid != -1:
            # Agora encontrar o último índice j >= first_valid com arr[j] <= right
            low = first_valid
            high = n - 1
            last_valid = -1
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] <= right:
                    last_valid = mid
                    low = mid + 1
                else:
                    high = mid - 1
            if last_valid != -1:
                count += (last_valid - first_valid + 1)
    print(count)

if __name__ == "__main__":
    main()
