n = int(input())

conta = 7

if n > 10:
    conta += min(n, 30) - 10
if n > 30:
    conta += (min(n, 100) - 30) * 2
if n > 100:
    conta += (n - 100) * 5

print(conta)