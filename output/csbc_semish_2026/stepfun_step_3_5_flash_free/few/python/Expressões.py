import sys

def is_valid(s):
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in '([{':
            stack.append(char)
        else:
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
    return not stack

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    t = int(data[0])
    strings = data[1:1+t]
    out_lines = []
    for s in strings:
        out_lines.append('S' if is_valid(s) else 'N')
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()