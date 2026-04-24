import sys
sys.setrecursionlimit(200000)

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    events = []
    idx = 1
    for _ in range(n):
        typ = data[idx]
        val = int(data[idx+1])
        idx += 2
        events.append((typ, val))
    
    # Processamento
    time_passed = 1  # tempo padrão entre eventos consecutivos
    pending = {}  # amigo -> tempo de recebimento
    total_time = {}  # amigo -> soma dos tempos de resposta
    answered = {}  # amigo -> booleano indicando se todas as mensagens foram respondidas
    
    for i in range(n):
        typ, x = events[i]
        if typ == 'T':
            time_passed = x
            continue
        elif typ == 'R':
            pending[x] = 0  # armazena tempo acumulado até agora
            if x not in total_time:
                total_time[x] = 0
                answered[x] = True
        elif typ == 'E':
            if x in pending:
                total_time[x] += pending[x]
                del pending[x]
            else:
                # resposta sem recebimento prévio? inválido, marca amigo como -1
                answered[x] = False
        
        # incrementa tempo acumulado para todas as mensagens pendentes
        for friend in pending:
            pending[friend] += time_passed
        time_passed = 1  # reset para próximo evento
    
    # amigos com mensagens pendentes recebem -1
    for friend in pending:
        answered[friend] = False
    
    # saída em ordem crescente de identificador
    friends = sorted(total_time.keys())
    out_lines = []
    for f in friends:
        if answered.get(f, True):
            out_lines.append(f"{f} {total_time[f]}")
        else:
            out_lines.append(f"{f} -1")
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()