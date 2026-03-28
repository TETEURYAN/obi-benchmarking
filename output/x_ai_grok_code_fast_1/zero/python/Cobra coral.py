
import sys

input = sys.stdin.read
data = input().split()
a, b, c, d = map(int, data)
nums = [a, b, c, d]

freq = {}
for n in nums:
    freq[n] = freq.get(n, 0) + 1

# Verificar se há exatamente um número com freq 2 e dois com freq 1
freq_values = list(freq.values())
if freq_values.count(2) == 1 and freq_values.count(1) == 2:
    # Encontrar o número que aparece duas vezes
    repeated = None
    for k, v in freq.items():
        if v == 2:
            repeated = k
            break
    # Encontrar posições (0-based)
    positions = [i for i in range(4) if nums[i] == repeated]
    pos1, pos2 = positions
    if pos1 % 2 == pos2 % 2:
        print("V")
    else:
        print("F")
else:
    # Embora o problema diga que sempre é uma ou outra, mas para segurança
    print("F")
