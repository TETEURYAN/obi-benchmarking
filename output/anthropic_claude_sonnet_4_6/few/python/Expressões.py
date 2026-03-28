import sys

def is_valid(s):
    stack = []
    matching = {')': '(', ']': '[', '}': '{'}
    for c in s:
        if c in '([{':
            stack.append(c)
        else:
            if not stack or stack[-1] != matching[c]:
                return False
            stack.pop()
    return len(stack) == 0

data = sys.stdin.read().split('\n')
T = int(data[0])
for i in range(1, T + 1):
    if i < len(data):
        s = data[i]
    else:
        s = ''
    print('S' if is_valid(s) else 'N')