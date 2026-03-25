import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

s = input_data[0]

suits = {'C': set(), 'E': set(), 'U': set(), 'P': set()}
errors = {'C': False, 'E': False, 'U': False, 'P': False}

for i in range(0, len(s), 3):
    val = s[i:i+2]
    suit = s[i+2]
    
    if val in suits[suit]:
        errors[suit] = True
    else:
        suits[suit].add(val)

for suit in ['C', 'E', 'U', 'P']:
    if errors[suit]:
        print("erro")
    else:
        print(13 - len(suits[suit]))