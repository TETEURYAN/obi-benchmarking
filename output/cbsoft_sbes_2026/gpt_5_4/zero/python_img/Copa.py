k = int(input().strip())
l = int(input().strip())

fase = ["oitavas", "quartas", "semifinal", "final"]
i = 0

while True:
    if (k + 1) // 2 == (l + 1) // 2:
        print(fase[i])
        break
    k = (k + 1) // 2
    l = (l + 1) // 2
    i += 1