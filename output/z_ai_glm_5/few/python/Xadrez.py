import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

L = int(input_data[0])
C = int(input_data[1])

# A casa (1, 1) é branca (1).
# A cor de uma casa (l, c) é determinada pela paridade da soma l + c.
# Se (l + c) é par, a cor é a mesma de (1, 1), ou seja, branca (1).
# Se (l + c) é ímpar, a cor é diferente, ou seja, preta (0).
# O canto inferior direito é a casa (L, C).

if (L + C) % 2 == 0:
    print(1)
else:
    print(0)