import sys

data = sys.stdin.read().strip()
naipes = ['C', 'E', 'U', 'P']
total = {n: 0 for n in naipes}
unicos = {n: set() for n in naipes}

n = len(data)
for i in range(0, n, 3):
    valor_str = data[i:i+2]
    naipe = data[i+2]
    valor = int(valor_str)
    if naipe in total:
        total[naipe] += 1
        unicos[naipe].add(valor)

for naipe in naipes:
    if total[naipe] != len(unicos[naipe]):
        print("erro")
    else:
        print(13 - len(unicos[naipe]))