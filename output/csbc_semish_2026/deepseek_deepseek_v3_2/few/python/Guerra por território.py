import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    arr = list(map(int, data[1:1+n]))
    
    total = sum(arr)
    prefix = 0
    for i in range(n):
        prefix += arr[i]
        if prefix == total - prefix:
            print(i+1)
            return

if __name__ == "__main__":
    main()