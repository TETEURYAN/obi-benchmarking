
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    matrix = []
    index = 1
    for i in range(n):
        row = list(map(int, data[index:index+n]))
        matrix.append(row)
        index += n

    min_total = float('inf')

    for i in range(n):
        for j in range(n - i):
            total = 0
            for k in range(i + 1):
                for l in range(j, j + i + 1 - k):
                    total += matrix[k][l]
            if total < min_total:
                min_total = total

    print(min_total)

if __name__ == "__main__":
    main()
