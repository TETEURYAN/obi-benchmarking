import sys

line = sys.stdin.read().strip()

suits = {'C': set(), 'E': set(), 'U': set(), 'P': set()}
duplicates = {'C': False, 'E': False, 'U': False, 'P': False}

i = 0
while i + 2 < len(line):
    card = line[i:i+3]
    dd = card[0:2]
    n = card[2]
    if n in suits:
        if dd in suits[n]:
            duplicates[n] = True
        else:
            suits[n].add(dd)
    i += 3

order = ['C', 'E', 'U', 'P']
for s in order:
    if duplicates[s]:
        print("erro")
    else:
        missing = 13 - len(suits[s])
        print(missing)