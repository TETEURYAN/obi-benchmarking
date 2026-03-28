import sys
from collections import Counter

input_str = sys.stdin.read().strip()
naipes = {'C': Counter(), 'E': Counter(), 'U': Counter(), 'P': Counter()}

for i in range(0, len(input_str), 3):
    carta = input_str[i:i+3]
    valor = carta[:2]
    naipe = carta[2]
    if naipe in naipes:
        naipes[naipe][valor] += 1

for n in ['C', 'E', 'U', 'P']:
    counter = naipes[n]
    if any(count > 1 for count in counter.values()):
        print("erro")
    else:
        faltam = 13 - len(counter)
        print(faltam)