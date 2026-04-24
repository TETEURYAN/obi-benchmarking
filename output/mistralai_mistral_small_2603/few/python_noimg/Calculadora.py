
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    operations = data[1:]

    result = 1
    for i in range(n):
        num = int(operations[2*i])
        op = operations[2*i + 1]
        if op == '*':
            result *= num
        else:
            result //= num

    print(result)

if __name__ == "__main__":
    main()
