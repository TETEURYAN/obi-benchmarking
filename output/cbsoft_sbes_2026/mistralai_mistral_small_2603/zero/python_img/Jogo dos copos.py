
n = int(input().strip())
moeda = input().strip()
for _ in range(n):
    movimento = int(input().strip())
    if movimento == 1:
        if moeda == 'A':
            moeda = 'B'
        elif moeda == 'B':
            moeda = 'A'
    elif movimento == 2:
        if moeda == 'B':
            moeda = 'C'
        elif moeda == 'C':
            moeda = 'B'
    elif movimento == 3:
        if moeda == 'A':
            moeda = 'C'
        elif moeda == 'C':
            moeda = 'A'
print(moeda)
