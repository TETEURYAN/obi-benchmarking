
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        print(-1)
        return

    n = int(data[0])
    m = int(data[1])
    A = list(map(int, data[2:2+n]))

    total = 0
    prev = 0
    for i in range(n):
        a = A[i]
        if a < 0 or a > m:
            print(-1)
            return

        if i == 0:
            if a <= m:
                total += min(a, m - a)
                prev = a
            else:
                print(-1)
                return
        else:
            if a >= prev:
                total += a
                prev = a
            else:
                if m - a >= prev:
                    total += m - a
                    prev = m - a
                else:
                    print(-1)
                    return

    print(total)

if __name__ == "__main__":
    main()
