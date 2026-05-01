n = int(input())

total = 7

if n <= 10:
    print(total)
else:
    # faixa 11-30: R$ 1,00 por m³
    # faixa 31-100: R$ 2,00 por m³
    # faixa 101+: R$ 5,00 por m³
    
    if n >= 11:
        consumo_faixa1 = min(n, 30) - 10
        total += consumo_faixa1 * 1
    
    if n >= 31:
        consumo_faixa2 = min(n, 100) - 30
        total += consumo_faixa2 * 2
    
    if n >= 101:
        consumo_faixa3 = n - 100
        total += consumo_faixa3 * 5
    
    print(total)