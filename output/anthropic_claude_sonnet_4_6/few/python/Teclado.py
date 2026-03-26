import sys

def char_to_digit(c):
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
    return mapping.get(c, '')

data = sys.stdin.read().splitlines()
N = data[0].strip()
M = int(data[1].strip())
count = 0
for i in range(M):
    word = data[2 + i].strip()
    converted = ''.join(char_to_digit(c) for c in word)
    if converted == N:
        count += 1
print(count)