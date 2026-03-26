
a, b, c, d = map(int, input().split())

# Verdadeira: BVBPBVBP -> padrão de 4: posições 0,1,2,3 = B,V,B,P
# então a==c e a!=b e a!=d e b!=d
# Falsa: BVPBVPBVP -> padrão de 4: posições 0,1,2,3 = B,V,P,B
# então a==d e a!=b e a!=c e b!=c

if a == c and a != b and a != d and b != d:
    print("V")
else:
    print("F")
