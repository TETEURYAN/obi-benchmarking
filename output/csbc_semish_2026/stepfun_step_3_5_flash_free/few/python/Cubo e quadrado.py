import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    A = int(data[0])
    B = int(data[1])
    count = 0
    k = 1
    while True:
        val = k**6
        if val > B:
            break
        if val >= A:
            count += 1
        k += 1
    print(count)

if __name__ == "__main__":
    main()