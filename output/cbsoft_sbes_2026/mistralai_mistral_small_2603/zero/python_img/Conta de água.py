
def calcular_conta_agua(consumo):
    assinatura = 7
    if consumo <= 10:
        return assinatura
    else:
        valor = assinatura
        if consumo > 10:
            consumo -= 10
            if consumo <= 20:
                valor += consumo * 1
            else:
                valor += 20 * 1
                consumo -= 20
                if consumo <= 70:
                    valor += consumo * 2
                else:
                    valor += 70 * 2
                    consumo -= 70
                    valor += consumo * 5
        return valor

n = int(input())
print(calcular_conta_agua(n))
