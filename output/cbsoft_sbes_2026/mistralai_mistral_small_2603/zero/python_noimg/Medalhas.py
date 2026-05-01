
t1 = int(input())
t2 = int(input())
t3 = int(input())

tempos = [(t1, 1), (t2, 2), (t3, 3)]
tempos_ordenados = sorted(tempos, key=lambda x: x[0])

print(tempos_ordenados[0][1])
print(tempos_ordenados[1][1])
print(tempos_ordenados[2][1])
