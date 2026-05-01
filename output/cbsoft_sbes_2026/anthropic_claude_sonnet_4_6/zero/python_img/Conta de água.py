n = int(input())
total = 7

if n > 10:
    faixa1 = min(n, 30) - 10
    total += faixa1 * 1

if n > 30:
    faixa2 = min(n, 100) - 30
    total += faixa2 * 2

if n > 100:
    faixa3 = n - 100
    total += faixa3 * 5

print(total)