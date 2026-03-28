import sys
from collections import defaultdict

input_data = sys.stdin.read().split()
N = int(input_data[0])
registros = []
idx = 1
for i in range(N):
    tipo = input_data[idx]
    x = int(input_data[idx + 1])
    registros.append((tipo, x))
    idx += 2

tempo = 0
eventos = []
for i in range(len(registros)):
    reg = registros[i]
    if reg[0] != 'T':
        eventos.append((reg[0], reg[1], tempo))
        if i + 1 < len(registros) and registros[i + 1][0] == 'T':
            tempo += registros[i + 1][1]
        else:
            tempo += 1

recebidas = defaultdict(list)
enviadas = defaultdict(list)
for tipo, amigo, t in eventos:
    if tipo == 'R':
        recebidas[amigo].append(t)
    elif tipo == 'E':
        enviadas[amigo].append(t)

result = {}
for amigo in sorted(set(recebidas.keys()) | set(enviadas.keys())):
    r_times = recebidas[amigo]
    e_times = enviadas[amigo]
    if len(r_times) != len(e_times):
        result[amigo] = -1
    else:
        total = 0
        for r, e in zip(r_times, e_times):
            total += e - r
        result[amigo] = total

for amigo in sorted(result.keys()):
    print(amigo, result[amigo])