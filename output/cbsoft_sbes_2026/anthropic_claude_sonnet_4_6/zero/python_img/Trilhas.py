import sys

def calc_esforco(altitudes):
    esforco = 0
    for i in range(1, len(altitudes)):
        diff = altitudes[i] - altitudes[i-1]
        if diff > 0:
            esforco += diff
    return esforco

def melhor_trilha(trilhas):
    melhor_id = -1
    melhor_esforco = float('inf')
    
    for i, altitudes in enumerate(trilhas):
        esforco_forward = calc_esforco(altitudes)
        esforco_backward = calc_esforco(altitudes[::-1])
        esforco = min(esforco_forward, esforco_backward)
        
        if esforco < melhor_esforco:
            melhor_esforco = esforco
            melhor_id = i + 1
    
    return melhor_id

input_data = sys.stdin.read().split()
idx = 0
N = int(input_data[idx]); idx += 1

trilhas = []
for _ in range(N):
    M = int(input_data[idx]); idx += 1
    altitudes = [int(input_data[idx + j]) for j in range(M)]
    idx += M
    trilhas.append(altitudes)

print(melhor_trilha(trilhas))