
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    t = int(data[0])
    strings = data[1:t+1]
    results = []
    for s in strings:
        stack = []
        valid = True
        for char in s:
            if char in '([{':
                stack.append(char)
            else:
                if not stack:
                    valid = False
                    break
                top = stack.pop()
                if (top == '(' and char != ')') or \
                   (top == '[' and char != ']') or \
                   (top == '{' and char != '}'):
                    valid = False
                    break
        if stack:
            valid = False
        results.append('S' if valid else 'N')
    print('\n'.join(results))

if __name__ == '__main__':
    main()
