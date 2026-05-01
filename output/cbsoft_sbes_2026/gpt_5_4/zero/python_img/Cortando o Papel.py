import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    a = data[1:1+n]

    events = []
    prev = 0
    for h in a:
        if h > prev:
            events.append((prev + 1, 1))
            events.append((h + 1, -1))
        elif h < prev:
            events.append((h + 1, 1))
            events.append((prev + 1, -1))
        prev = h

    if not events:
        print(0)
        return

    events.sort()
    cur = 0
    ans = 0
    i = 0
    m = len(events)
    while i < m:
        x = events[i][0]
        delta = 0
        while i < m and events[i][0] == x:
            delta += events[i][1]
            i += 1
        cur += delta
        if cur > ans:
            ans = cur

    print(ans)

if __name__ == "__main__":
    main()
