
mapping = {}
keys = {
    '2': 'ABC',
    '3': 'DEF',
    '4': 'GHI',
    '5': 'JKL',
    '6': 'MNO',
    '7': 'PQRS',
    '8': 'TUV',
    '9': 'WXYZ'
}

for digit, letters in keys.items():
    for letter in letters:
        mapping[letter] = digit

line = input().strip()
result = []
for ch in line:
    if ch == '-':
        result.append('-')
    elif ch in mapping:
        result.append(mapping[ch])
    else:
        result.append(ch)

print(''.join(result))