
def calcular_conta_agua(consumo):
    if consumo <= 10:
        return 7
    else:
        valor = 7
        if consumo > 10:
            valor += (min(consumo, 30) - 10) * 1
        if consumo > 30:
            valor += (min(consumo, 100) - 30) * 2
        if consumo > 100:
            valor += (consumo - 100) * 5
        return valor

N = int(input())
print(calcular_conta_agua(N))
