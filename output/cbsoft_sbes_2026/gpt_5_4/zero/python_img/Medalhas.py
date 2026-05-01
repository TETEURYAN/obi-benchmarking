t1 = int(input())
t2 = int(input())
t3 = int(input())

tempos = [(t1, 1), (t2, 2), (t3, 3)]
tempos.sort()

for _, nadador in tempos:
    print(nadador)