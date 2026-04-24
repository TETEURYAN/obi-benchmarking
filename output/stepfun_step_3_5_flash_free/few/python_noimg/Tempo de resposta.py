import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    registros = []
    idx = 1
    for _ in range(n):
        tipo = data[idx]; idx += 1
        x = int(data[idx]); idx += 1
        registros.append((tipo, x))
    
    tempo_atual = 0
    eventos_por_amigo = {}
    i = 0
    while i < len(registros):
        tipo, x = registros[i]
        if tipo == 'T':
            tempo_atual += x
            i += 1
        else:  # 'R' ou 'E'
            amigo = x
            if amigo not in eventos_por_amigo:
                eventos_por_amigo[amigo] = []
            eventos_por_amigo[amigo].append((tipo, tempo_atual))
            i += 1
            if i < len(registros) and registros[i][0] in ('R', 'E'):
                tempo_atual += 1
    
    resultados = []
    for amigo in sorted(eventos_por_amigo.keys()):
        eventos = eventos_por_amigo[amigo]
        pendente = None
        total = 0
        valido = True
        for tipo, tempo in eventos:
            if tipo == 'R':
                if pendente is not None:
                    valido = False
                    break
                pendente = tempo
            else:  # 'E'
                if pendente is None:
                    valido = False
                    break
                total += tempo - pendente
                pendente = None
        if pendente is not None:
            valido = False
        if not valido:
            total = -1
        resultados.append((amigo, total))
    
    for amigo, total in resultados:
        print(amigo, total)

if __name__ == "__main__":
    main()