
def mapear_tecla(c):
    if c in 'abc':
        return '2'
    elif c in 'def':
        return '3'
    elif c in 'ghi':
        return '4'
    elif c in 'jkl':
        return '5'
    elif c in 'mno':
        return '6'
    elif c in 'pqrs':
        return '7'
    elif c in 'tuv':
        return '8'
    elif c in 'wxyz':
        return '9'
    return ''

n = input().strip()
m = int(input().strip())
contador = 0

for _ in range(m):
    palavra = input().strip()
    mapeamento = []
    for c in palavra:
        mapeamento.append(mapear_tecla(c))
    if ''.join(mapeamento) == n:
        contador += 1

print(contador)
