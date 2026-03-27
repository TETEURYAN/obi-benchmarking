import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    dados = []
    index = 1
    for _ in range(n):
        dado = list(map(int, data[index:index+6]))
        index += 6
        dados.append(dado)

    max_soma = 0
    for lado in range(4):
        soma = 0
        for i in range(n):
            if i == 0:
                soma += dados[i][lado]
            else:
                topo_abaixo = dados[i-1][2]
                for face in range(6):
                    if dados[i][face] == topo_abaixo:
                        if face == 0:
                            soma += dados[i][lado]
                        elif face == 1:
                            if lado == 0:
                                soma += dados[i][3]
                            elif lado == 1:
                                soma += dados[i][2]
                            elif lado == 2:
                                soma += dados[i][0]
                            elif lado == 3:
                                soma += dados[i][1]
                        elif face == 2:
                            if lado == 0:
                                soma += dados[i][4]
                            elif lado == 1:
                                soma += dados[i][5]
                            elif lado == 2:
                                soma += dados[i][1]
                            elif lado == 3:
                                soma += dados[i][0]
                        elif face == 3:
                            if lado == 0:
                                soma += dados[i][5]
                            elif lado == 1:
                                soma += dados[i][4]
                            elif lado == 2:
                                soma += dados[i][0]
                            elif lado == 3:
                                soma += dados[i][1]
                        elif face == 4:
                            if lado == 0:
                                soma += dados[i][2]
                            elif lado == 1:
                                soma += dados[i][3]
                            elif lado == 2:
                                soma += dados[i][5]
                            elif lado == 3:
                                soma += dados[i][4]
                        elif face == 5:
                            if lado == 0:
                                soma += dados[i][3]
                            elif lado == 1:
                                soma += dados[i][2]
                            elif lado == 2:
                                soma += dados[i][4]
                            elif lado == 3:
                                soma += dados[i][5]
                        break
        if soma > max_soma:
            max_soma = soma
    print(max_soma)

if __name__ == "__main__":
    main()