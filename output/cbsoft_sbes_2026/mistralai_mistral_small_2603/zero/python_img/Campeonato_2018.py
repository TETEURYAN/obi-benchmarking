
def main():
    posicoes = list(map(int, input().split()))
    master_kung = 1
    master_lu = 9

    pos_kung = posicoes.index(master_kung) + 1
    pos_lu = posicoes.index(master_lu) + 1

    if pos_kung > pos_lu:
        pos_kung, pos_lu = pos_lu, pos_kung

    fase = None
    if pos_lu - pos_kung == 1:
        if pos_kung % 2 == 1:
            fase = 'oitavas'
        else:
            fase = 'oitavas'
    elif pos_lu - pos_kung <= 2:
        fase = 'quartas'
    elif pos_lu - pos_kung <= 4:
        fase = 'semifinal'
    else:
        fase = 'final'

    print(fase)

if __name__ == '__main__':
    main()
