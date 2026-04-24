import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    a = list(map(int, data[1:1+n]))
    m = n - 1
    count_neg = 0
    for i in range(n):
        if (i | m) == m:
            if a[i] == -1:
                count_neg += 1
    print("branca" if count_neg % 2 else "preta")

if __name__ == "__main__":
    main()