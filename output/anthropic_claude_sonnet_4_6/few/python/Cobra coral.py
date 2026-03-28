import sys
a, b, c, d = map(int, sys.stdin.read().split())

# Verdadeira: BVBPBVBP -> padrão: pos0==pos2, pos1!=pos0, pos3!=pos1, pos3!=pos2, pos1!=pos3
# Falsa: BVPBVPBV -> padrão: pos0==pos3, pos1!=pos0, pos2!=pos1, pos2!=pos0

# Verdadeira coral pattern: a b a c (where a!=b, a!=c, b!=c)
# a==c, a!=b, a!=d, b!=d
if a == c and a != b and a != d and b != d:
    print("V")
else:
    print("F")