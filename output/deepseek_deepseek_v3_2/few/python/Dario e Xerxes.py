import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    idx = 0
    n = int(data[idx])
    idx += 1
    wins_dario = 0
    wins_xerxes = 0
    # Regras de vitória conforme a figura descrita:
    # 0 perde para 1, 2, 3
    # 1 perde para 2, 3, 4
    # 2 perde para 3, 4, 0
    # 3 perde para 4, 0, 1
    # 4 perde para 0, 1, 2
    # Podemos verificar se (X - D) mod 5 é 1, 2 ou 3 → Xerxes ganha
    # Caso contrário, Dario ganha.
    for _ in range(n):
        d = int(data[idx])
        x = int(data[idx + 1])
        idx += 2
        diff = (x - d) % 5
        if diff == 1 or diff == 2 or diff == 3:
            wins_xerxes += 1
        else:
            wins_dario += 1
    if wins_dario > wins_xerxes:
        print("dario")
    else:
        print("xerxes")

if __name__ == "__main__":
    main()