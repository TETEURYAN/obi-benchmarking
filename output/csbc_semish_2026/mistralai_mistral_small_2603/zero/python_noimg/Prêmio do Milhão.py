
n = int(input())
total = 0
dias = 0
for _ in range(n):
    acessos = int(input())
    total += acessos
    dias += 1
    if total >= 1000000:
        print(dias)
        break
