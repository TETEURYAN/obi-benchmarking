import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    V = int(data[0])
    contas = list(map(int, data[1:4]))
    contas.sort()
    soma = 0
    count = 0
    for valor in contas:
        if soma + valor <= V:
            soma += valor
            count += 1
        else:
            break
    print(count)

if __name__ == "__main__":
    main()