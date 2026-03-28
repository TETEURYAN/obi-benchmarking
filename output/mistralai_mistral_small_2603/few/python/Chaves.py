import sys

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        print('N')
        return

    n = int(data[0])
    code = ''.join(data[1:1+n])

    stack = []
    for char in code:
        if char == '{':
            stack.append(char)
        elif char == '}':
            if not stack:
                print('N')
                return
            stack.pop()

    print('S' if not stack else 'N')

if __name__ == "__main__":
    main()