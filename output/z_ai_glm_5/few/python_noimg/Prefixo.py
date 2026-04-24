import sys

def main():
    data = sys.stdin.read().split()
    
    if not data:
        return

    n = int(data[0])
    p1 = data[1]
    m = int(data[2])
    p2 = data[3]

    count = 0
    limit = min(n, m)

    for i in range(limit):
        if p1[i] == p2[i]:
            count += 1
        else:
            break

    print(count)

if __name__ == "__main__":
    main()