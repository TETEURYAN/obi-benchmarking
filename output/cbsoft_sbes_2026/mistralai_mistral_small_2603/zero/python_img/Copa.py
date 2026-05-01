
def determinar_fase(k, l):
    if k > l:
        k, l = l, k
    if l - k == 1 and k % 2 == 1:
        return "oitavas"
    elif l - k == 2 and k % 4 == 1:
        return "quartas"
    elif l - k == 4 and k % 8 == 1:
        return "semifinal"
    else:
        return "final"

k = int(input())
l = int(input())
print(determinar_fase(k, l))
