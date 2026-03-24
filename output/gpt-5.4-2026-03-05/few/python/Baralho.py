import sys

s = sys.stdin.read().strip()

seen = {'C': set(), 'E': set(), 'U': set(), 'P': set()}
error = {'C': False, 'E': False, 'U': False, 'P': False}

for i in range(0, len(s), 3):
    card = s[i:i+3]
    num = card[:2]
    suit = card[2]
    if num in seen[suit]:
        error[suit] = True
    else:
        seen[suit].add(num)

for suit in ['C', 'E', 'U', 'P']:
    if error[suit]:
        print('erro')
    else:
        print(13 - len(seen[suit]))