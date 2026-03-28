import sys

p = sys.stdin.read().strip()

vogais = set('aeiou')
vogal_map = {
    'b': 'a', 'c': 'a', 'd': 'e', 'f': 'e', 'g': 'e', 'h': 'i',
    'j': 'i', 'k': 'i', 'l': 'i', 'm': 'o', 'n': 'o', 'p': 'o',
    'q': 'o', 'r': 'o', 's': 'u', 't': 'u', 'v': 'u', 'x': 'u', 'z': 'u'
}
next_conso = {
    'b': 'c', 'c': 'd', 'd': 'f', 'f': 'g', 'g': 'h', 'h': 'j',
    'j': 'k', 'k': 'l', 'l': 'm', 'm': 'n', 'n': 'p', 'p': 'q',
    'q': 'r', 'r': 's', 's': 't', 't': 'v', 'v': 'x', 'x': 'z', 'z': 'z'
}

result = ''
for letra in p:
    if letra in vogais:
        result += letra
    else:
        result += letra + vogal_map[letra] + next_conso[letra]

print(result)