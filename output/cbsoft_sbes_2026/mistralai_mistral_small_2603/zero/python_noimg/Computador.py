
import sys

def main():
    data = sys.stdin.read().split()
    ptr = 0
    N = int(data[ptr])
    ptr += 1
    M = int(data[ptr])
    ptr += 1

    memory = [0] * (N + 2)

    output = []
    for _ in range(M):
        op = int(data[ptr])
        ptr += 1
        if op == 1:
            i = int(data[ptr])
            ptr += 1
            v = int(data[ptr])
            ptr += 1
            j = i
            val = v
            while val > 0 and j <= N:
                memory[j] += val
                j += 1
                val -= 1
        elif op == 2:
            i = int(data[ptr])
            ptr += 1
            v = int(data[ptr])
            ptr += 1
            j = i
            val = v
            while val > 0 and j >= 1:
                memory[j] += val
                j -= 1
                val -= 1
        elif op == 3:
            i = int(data[ptr])
            ptr += 1
            output.append(str(memory[i]))

    print('\n'.join(output))

if __name__ == '__main__':
    main()
