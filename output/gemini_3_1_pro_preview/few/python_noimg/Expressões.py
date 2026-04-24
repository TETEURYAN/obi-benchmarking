import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

t = int(input_data[0])
strings = input_data[1:t+1]

match = {')': '(', ']': '[', '}': '{'}

for s in strings:
    stack = []
    valid = True
    for char in s:
        if char in "([{":
            stack.append(char)
        else:
            if not stack or stack[-1] != match[char]:
                valid = False
                break
            stack.pop()
    
    if valid and not stack:
        print("S")
    else:
        print("N")