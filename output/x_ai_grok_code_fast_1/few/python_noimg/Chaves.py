import sys

input_data = sys.stdin.read().splitlines()
N = int(input_data[0])
code = ''.join(input_data[1:])
stack = []
for char in code:
    if char == '{':
        stack.append(char)
    elif char == '}':
        if not stack:
            print('N')
            sys.exit(0)
        stack.pop()
if not stack:
    print('S')
else:
    print('N')