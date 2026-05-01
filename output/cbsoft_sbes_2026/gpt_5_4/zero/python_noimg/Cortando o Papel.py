import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n = data[0]
    a = data[1:1+n]

    events = {}

    for i, h in enumerate(a):
        events[h] = events.get(h, 0) - 1
        if i == 0 or a[i - 1] < h:
            events[h] = events.get(h, 0) + 1
        if i == n - 1 or a[i + 1] < h:
            events[h] = events.get(h, 0) + 1

    cur = 0
    ans = 0
    for h in sorted(events):
        cur += events[h]
        if cur > ans:
            ans = cur

    print(ans)

if __name__ == "__main__":
    main()
