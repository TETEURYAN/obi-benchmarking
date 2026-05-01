
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return
    n = int(data[0])
    A = list(map(int, data[1:n+1]))

    max_count = 0
    for i in range(n):
        if A[i] == 0:
            continue
        current = A[i]
        count = 1
        for j in range(i-1, -1, -1):
            if A[j] == 0:
                continue
            k = current - (i - j)
            if k >= 1 and k <= A[j]:
                count += 1
                current = k
            else:
                break
        if count > max_count:
            max_count = count
    print(max_count)

if __name__ == "__main__":
    main()
