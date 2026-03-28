import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    a = list(map(int, data[1:1+n]))
    if n == 1:
        print(1)
        return
    d = [a[i+1] - a[i] for i in range(n-1)]
    count = 0
    i = 0
    while i < len(d):
        j = i + 1
        while j < len(d) and d[j] == d[i]:
            j += 1
        count += 1
        i = j
    print(count)

if __name__ == "__main__":
    main()