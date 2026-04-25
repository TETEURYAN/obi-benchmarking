import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()

N = data[0]
M = int(data[1])
words = data[2:2 + M]

mp = {
    'a': '2', 'b': '2', 'c': '2',
    'd': '3', 'e': '3', 'f': '3',
    'g': '4', 'h': '4', 'i': '4',
    'j': '5', 'k': '5', 'l': '5',
    'm': '6', 'n': '6', 'o': '6',
    'p': '7', 'q': '7', 'r': '7', 's': '7',
    't': '8', 'u': '8', 'v': '8',
    'w': '9', 'x': '9', 'y': '9', 'z': '9'
}

target_len = len(N)
ans = 0

for w in words:
    if len(w) != target_len:
        continue
    ok = True
    for i, ch in enumerate(w):
        if mp[ch] != N[i]:
            ok = False
            break
    if ok:
        ans += 1

print(ans)