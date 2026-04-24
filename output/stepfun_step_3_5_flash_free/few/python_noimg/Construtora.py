import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    a = list(map(int, data[1:1+n]))
    M = max(a)
    d = [M - x for x in a]
    ans = 0
    prev = 0
    for x in d:
        if x > prev:
            ans += x - prev
        prev = x
    print(ans)

if __name__ == "__main__":
    main()