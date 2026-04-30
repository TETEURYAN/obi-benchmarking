
import sys

mapping = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}

N = sys.stdin.readline().strip()
M = int(sys.stdin.readline().strip())

count = 0
for _ in range(M):
    word = sys.stdin.readline().strip()
    if len(word) != len(N):
        continue
    match = True
    for i, digit in enumerate(N):
        if word[i] not in mapping[digit]:
            match = False
            break
    if match:
        count += 1

print(count)
