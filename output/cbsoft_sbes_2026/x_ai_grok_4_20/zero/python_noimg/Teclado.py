
import sys

mapping = {
    'a': '2', 'b': '2', 'c': '2',
    'd': '3', 'e': '3', 'f': '3',
    'g': '4', 'h': '4', 'i': '4',
    'j': '5', 'k': '5', 'l': '5',
    'm': '6', 'n': '6', 'o': '6',
    'p': '7', 'q': '7', 'r': '7', 's': '7',
    't': '8', 'u': '8', 'v': '8',
    'w': '9', 'x': '9', 'y': '9', 'z': '9'
}

N = sys.stdin.readline().strip()
M = int(sys.stdin.readline().strip())

count = 0
for _ in range(M):
    word = sys.stdin.readline().strip()
    if len(word) != len(N):
        continue
    match = True
    for i, char in enumerate(word):
        if mapping[char] != N[i]:
            match = False
            break
    if match:
        count += 1

print(count)
