import sys

def main():
    data = sys.stdin.read().split()
    ptr = 0
    test_case = 1
    output_lines = []

    while ptr < len(data):
        X1 = int(data[ptr])
        Y1 = int(data[ptr+1])
        X2 = int(data[ptr+2])
        Y2 = int(data[ptr+3])
        ptr += 4

        if X1 == 0 and Y1 == 0 and X2 == 0 and Y2 == 0:
            break

        N = int(data[ptr])
        ptr += 1

        count = 0
        for _ in range(N):
            X = int(data[ptr])
            Y = int(data[ptr+1])
            ptr += 2
            if X1 <= X <= X2 and Y2 <= Y <= Y1:
                count += 1

        output_lines.append(f"Teste {test_case}")
        output_lines.append(str(count))
        output_lines.append("")
        test_case += 1

    print("\n".join(output_lines))

if __name__ == "__main__":
    main()