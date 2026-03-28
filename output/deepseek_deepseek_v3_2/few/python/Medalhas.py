import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    t1, t2, t3 = map(int, data[:3])
    times = [(t1, 1), (t2, 2), (t3, 3)]
    times.sort(key=lambda x: x[0])
    for _, idx in times:
        print(idx)

if __name__ == "__main__":
    main()