import sys

def main():
    # Leitura rápida de todos os dados de entrada
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        R = int(next(iterator))
        N = int(next(iterator))
    except StopIteration:
        return

    # Array para armazenar o preço mínimo de cada tipo de fruta.
    # O problema diz que Ti está entre 1 e 100.
    # Inicializamos com infinito para indicar que o tipo ainda não foi encontrado.
    min_prices = [float('inf')] * 101

    for _ in range(N):
        try:
            t = int(next(iterator))
            p = int(next(iterator))
            # Queremos o menor preço para cada tipo de fruta
            if p < min_prices[t]:
                min_prices[t] = p
        except StopIteration:
            break

    # Coletar os preços mínimos das frutas que aparecem na entrada
    prices = []
    for i in range(1, 101):
        if min_prices[i] != float('inf'):
            prices.append(min_prices[i])

    # Ordenar os preços para aplicar a estratégia gulosa (greedy).
    # Para maximizar o número de itens, compramos os mais baratos primeiro.
    prices.sort()

    count = 0
    current_money = R

    for price in prices:
        if current_money >= price:
            current_money -= price
            count += 1
        else:
            # Como a lista está ordenada, se não podemos comprar este, não podemos comprar os próximos
            break

    print(count)

if __name__ == '__main__':
    main()