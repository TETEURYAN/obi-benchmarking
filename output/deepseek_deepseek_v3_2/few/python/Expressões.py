import sys

def is_valid(s: str) -> bool:
    stack = []
    matching = {')': '(', ']': '[', '}': '{'}
    for ch in s:
        if ch in '([{':
            stack.append(ch)
        else:
            if not stack or stack[-1] != matching[ch]:
                return False
            stack.pop()
    return not stack

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    t = int(data[0])
    out_lines = []
    for i in range(1, t + 1):
        s = data[i]
        out_lines.append('S' if is_valid(s) else 'N')
    sys.stdout.write('\n'.join(out_lines))

if __name__ == '__main__':
    main()