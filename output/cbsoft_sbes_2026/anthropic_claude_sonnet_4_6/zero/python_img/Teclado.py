letter_to_digit = {}
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

for digit, letters in mapping.items():
    for letter in letters:
        letter_to_digit[letter] = digit

N = input().strip()
M = int(input().strip())

count = 0
for _ in range(M):
    C = input().strip()
    if len(C) != len(N):
        continue
    match = True
    for i in range(len(N)):
        if letter_to_digit.get(C[i], '') != N[i]:
            match = False
            break
    if match:
        count += 1

print(count)