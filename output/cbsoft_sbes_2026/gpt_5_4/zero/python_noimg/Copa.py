k = int(input().strip())
l = int(input().strip())

fase = ["oitavas", "quartas", "semifinal", "final"]
i = 0

while k != l:
    k = (k + 1) // 2
    l = (l + 1) // 2
    i += 1

print(fase[i - 1])