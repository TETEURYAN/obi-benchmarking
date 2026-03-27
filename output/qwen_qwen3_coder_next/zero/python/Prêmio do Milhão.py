n = int(input())
acessos = []
for _ in range(n):
    acessos.append(int(input()))

total = 0
dias = 0
for i in range(n):
    total += acessos[i]
    dias += 1
    if total >= 1000000:
        break

print(dias)