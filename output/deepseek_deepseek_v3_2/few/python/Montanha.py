import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    a = list(map(int, data[1:1+n]))
    for i in range(1, n-1):
        if a[i-1] > a[i] < a[i+1]:
            print("S")
            return
    print("N")

if __name__ == "__main__":
    main()