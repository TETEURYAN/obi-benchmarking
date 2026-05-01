
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    arr = list(map(int, data[1:n+1]))
    arr.sort()
    count = 0
    for i in range(n-2):
        k = i + 2
        for j in range(i+1, n-1):
            while k < n and arr[i] + arr[j] > arr[k]:
                k += 1
            count += k - j - 1
    print(count)

if __name__ == "__main__":
    main()
