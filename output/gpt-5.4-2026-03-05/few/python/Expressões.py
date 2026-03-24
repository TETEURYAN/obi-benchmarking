import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()

t = int(data[0])
out = []

pairs = {')': '(', ']': '[', '}': '{'}
opens = set('([{')

for i in range(1, t + 1):
    s = data[i]
    stack = []
    ok = True
    for ch in s:
        if ch in opens:
            stack.append(ch)
        else:
            if not stack or stack[-1] != pairs[ch]:
                ok = False
                break
            stack.pop()
    if stack:
        ok = False
    out.append('S' if ok else 'N')

sys.stdout.write('\n'.join(out))