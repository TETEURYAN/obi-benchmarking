
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    t = int(data[1])
    cima = list(map(int, data[2:2+n]))
    baixo = list(map(int, data[2+n:2+2*n]))
    ops = []
    index = 2 + 2*n
    for i in range(t):
        I = int(data[index]) - 1
        J = int(data[index+1]) - 1
        ops.append((I, J))
        index += 2

    flip = [False] * n
    for I, J in ops:
        for i in range(I, J+1):
            flip[i] = not flip[i]

    result = []
    for i in range(n):
        if flip[i]:
            result.append(str(baixo[i]))
        else:
            result.append(str(cima[i]))

    print(' '.join(result))

if __name__ == "__main__":
    main()
