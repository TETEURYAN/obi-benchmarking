import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
min_price = float('inf')

idx = 1
for _ in range(n):
    p = float(input_data[idx])
    g = int(input_data[idx + 1])
    idx += 2
    
    # Calcula o preço para 1000 gramas (1 kg)
    # Preço por grama = P / G
    # Preço por kg = (P / G) * 1000
    cost = (p / g) * 1000
    
    if cost < min_price:
        min_price = cost

print("{:.2f}".format(min_price))