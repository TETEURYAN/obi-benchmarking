mapping = {}
for c in 'ABC':
    mapping[c] = '2'
for c in 'DEF':
    mapping[c] = '3'
for c in 'GHI':
    mapping[c] = '4'
for c in 'JKL':
    mapping[c] = '5'
for c in 'MNO':
    mapping[c] = '6'
for c in 'PQRS':
    mapping[c] = '7'
for c in 'TUV':
    mapping[c] = '8'
for c in 'WXYZ':
    mapping[c] = '9'

line = input()
result = []
for ch in line:
    if ch == '-':
        result.append('-')
    elif ch in mapping:
        result.append(mapping[ch])
    else:
        result.append(ch)
print(''.join(result))