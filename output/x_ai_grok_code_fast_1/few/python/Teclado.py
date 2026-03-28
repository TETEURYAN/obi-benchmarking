import sys

input_data = sys.stdin.read().split()
idx = 0
N = input_data[idx]
idx += 1
M = int(input_data[idx])
idx += 1
words = []
for _ in range(M):
    words.append(input_data[idx])
    idx += 1

keypad = {
    '2': set('abc'),
    '3': set('def'),
    '4': set('ghi'),
    '5': set('jkl'),
    '6': set('mno'),
    '7': set('pqrs'),
    '8': set('tuv'),
    '9': set('wxyz')
}

count = 0
for word in words:
    if len(word) != len(N):
        continue
    valid = True
    for i in range(len(N)):
        if word[i] not in keypad[N[i]]:
            valid = False
            break
    if valid:
        count += 1

print(count)