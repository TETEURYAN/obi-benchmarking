D = int(input())
resto = D % 400
print(min(resto, 400 - resto))