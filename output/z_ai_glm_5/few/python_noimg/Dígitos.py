import sys

# Aumentar o limite de recursão, embora a solução seja iterativa
sys.setrecursionlimit(200000)

def solve():
    # Leitura rápida de toda a entrada
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    # N é o número de dígitos
    N = int(input_data[0])
    
    # Os dígitos seguem na linha seguinte. 
    # input_data[1:] contém os dígitos como strings.
    # Juntamos para formar a sequência completa.
    S = "".join(input_data[1:])
    
    # Garantia de que pegamos apenas N caracteres (caso haja ruído, embora o problema garanta N)
    S = S[:N]

    # Função para somar 1 a um número representado como string
    def add_one(s):
        # Converte para lista de caracteres para modificação
        s_list = list(s)
        carry = 1
        # Itera do último dígito para o primeiro
        for i in range(len(s_list) - 1, -1, -1):
            if carry == 0:
                break
            
            digit = int(s_list[i]) + carry
            s_list[i] = str(digit % 10)
            carry = digit // 10
        
        # Se ainda houver carry, adiciona um novo dígito '1' no início
        if carry:
            return "1" + "".join(s_list)
        return "".join(s_list)

    # Itera sobre todos os possíveis tamanhos para A
    # O tamanho de A pode variar de 1 até N
    for length in range(1, N + 1):
        # Candidato a valor de A
        A_candidate = S[:length]
        
        # Pela restrição do problema, A >= 1. 
        # Números não podem ter leading zeros, a menos que o número seja 0 (mas A >= 1).
        # Se o primeiro dígito for '0', o candidato é inválido.
        if A_candidate[0] == '0':
            continue
        
        # Simula a sequência a partir de A
        current_val = A_candidate
        current_idx = length
        possible = True
        
        while current_idx < N:
            next_val = add_one(current_val)
            len_next = len(next_val)
            
            # Verifica se o próximo número cabe na sequência restante
            if current_idx + len_next > N:
                possible = False
                break
            
            # Compara o próximo valor calculado com o segmento correspondente na string S
            if S[current_idx : current_idx + len_next] == next_val:
                current_val = next_val
                current_idx += len_next
            else:
                possible = False
                break
        
        # Se a simulação consumiu toda a string, encontramos um A válido.
        # Como iteramos do menor tamanho para o maior, este é o menor A possível.
        if possible:
            print(A_candidate)
            return

if __name__ == '__main__':
    solve()