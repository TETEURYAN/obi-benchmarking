import sys

def is_valid(s):
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack:
                return False
            top = stack.pop()
            if top != mapping[char]:
                return False
    return not stack

data = sys.stdin.read().splitlines()
T = int(data[0])
for i in range(1, T + 1):
    s = data[i]
    if is_valid(s):
        print('S')
    else:
        print('N')