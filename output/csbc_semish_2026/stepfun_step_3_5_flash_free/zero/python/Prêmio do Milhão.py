
n = int(input().strip())
soma = 0
dias = 0
for _ in range(n):
    a = int(input().strip())
    soma += a
    dias += 1
    if soma >= 1000000:
        print(dias)
        break
