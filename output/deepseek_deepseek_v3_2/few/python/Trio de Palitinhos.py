import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    arr = list(map(int, data[1:1+n]))
    arr.sort()
    
    total = 0
    for i in range(n-2):
        k = i + 2
        for j in range(i+1, n-1):
            while k < n and arr[i] + arr[j] > arr[k]:
                k += 1
            total += k - j - 1
    print(total)

if __name__ == "__main__":
    main()