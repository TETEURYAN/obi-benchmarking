import sys

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        return
    n = int(data[0])
    stack = []
    for i in range(1, n + 1):
        line = data[i]
        for ch in line:
            if ch == '{':
                stack.append('{')
            elif ch == '}':
                if not stack:
                    print("N")
                    return
                stack.pop()
    if stack:
        print("N")
    else:
        print("S")

if __name__ == "__main__":
    main()