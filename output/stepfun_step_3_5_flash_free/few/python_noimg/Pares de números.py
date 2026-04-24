import sys

def count_pairs_leq(arr, X):
    n = len(arr)
    count = 0
    right = n - 1
    for left in range(n):
        while right > left and arr[left] + arr[right] > X:
            right -= 1
        if right <= left:
            break
        count += (right - left)
    return count

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    I = int(data[1])
    F = int(data[2])
    arr = list(map(int, data[3:3+n]))
    arr.sort()
    total = count_pairs_leq(arr, F) - count_pairs_leq(arr, I-1)
    print(total)

if __name__ == "__main__":
    main()