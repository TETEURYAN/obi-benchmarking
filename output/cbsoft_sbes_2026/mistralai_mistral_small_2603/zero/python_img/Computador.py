
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
        if op == 1 or op == 2:
            I = int(data[ptr])
            ptr += 1
            V = int(data[ptr])
            ptr += 1
            if op == 1:
                k = 0
                while V - k > 0 and I + k <= N:
                    memory[I + k] += V - k
                    k += 1
            else:
                k = 0
                while V - k > 0 and I - k >= 1:
                    memory[I - k] += V - k
                    k += 1
        else:
            I = int(data[ptr])
            ptr += 1
            output.append(str(memory[I]))

    print('\n'.join(output))

if __name__ == '__main__':
    main()
