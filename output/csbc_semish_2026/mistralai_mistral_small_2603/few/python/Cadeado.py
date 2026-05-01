import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    total_clicks = 0
    index = 1
    for _ in range(n):
        c = int(data[index])
        s = int(data[index + 1])
        index += 2
        diff = abs(c - s)
        total_clicks += min(diff, 10 - diff)
    print(total_clicks)

if __name__ == "__main__":
    main()