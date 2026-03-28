
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return

    L = int(data[0])
    C = int(data[1])
    matrix = []
    index = 2
    for i in range(L):
        row = list(map(int, data[index:index+C]))
        matrix.append(row)
        index += C

    max_elements = 0

    for i1 in range(L):
        for j1 in range(C):
            for i2 in range(i1, L):
                for j2 in range(j1, C):
                    valid = True
                    for i in range(i1+1, i2+1):
                        for j in range(j1+1, j2+1):
                            if (matrix[i1][j1] + matrix[i][j] > matrix[i1][j] + matrix[i][j1]):
                                valid = False
                                break
                        if not valid:
                            break
                    if valid:
                        elements = (i2 - i1 + 1) * (j2 - j1 + 1)
                        if elements > max_elements:
                            max_elements = elements
    print(max_elements)

if __name__ == "__main__":
    main()
