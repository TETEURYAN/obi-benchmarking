
import sys

def main():
    data = sys.stdin.read().split()
    ptr = 0
    test_num = 1
    while ptr < len(data):
        m = int(data[ptr])
        ptr += 1
        if m == 0:
            break
        expr = data[ptr]
        ptr += 1

        parts = []
        num = 0
        for c in expr:
            if c == '+' or c == '-':
                parts.append(num)
                parts.append(c)
                num = 0
            else:
                num = num * 10 + int(c)
        parts.append(num)

        result = parts[0]
        i = 1
        while i < len(parts):
            op = parts[i]
            next_num = parts[i+1]
            if op == '+':
                result += next_num
            else:
                result -= next_num
            i += 2

        print(f"Teste {test_num}")
        print(result)
        print()
        test_num += 1

if __name__ == "__main__":
    main()
